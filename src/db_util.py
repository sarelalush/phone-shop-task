#!/usr/bin/python

import yaml
import sqlite3
import os.path
import src.conf as conf




def create_db():
    if os.path.isfile(conf.DB_NAME):
        print("Database exist, skip create")
        return sqlite3.connect(f'file:{conf.DB_NAME}?mode=rw', uri=True)
    else:
        conn = sqlite3.connect(conf.DB_NAME)
        for table in conf.TABLES.values():
            conn.cursor().execute(table)
        return conn


def load_raw_data(conn):
    with open(r'db/raw_data.yaml') as file:
        records = yaml.load(file, Loader=yaml.FullLoader)
        for key in records.keys():
            for item in records[key]:
                conn.cursor().execute(
                    f"INSERT INTO {key} VALUES({records[key][item]})"
                )
                conn.commit()
                
                
def select_all_by_table(conn, table_name):
    print(f"\nAll data in table:{table_name}")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def add_new_phone(conn , newPhone):
    cur = conn.cursor()
    quantity = check_phone_exist(conn , newPhone.manufacturer , newPhone.model)
    if not quantity:
        cur.execute(f"INSERT INTO {conf.PHONE_TABLE} VALUES(?,?,?,?,?,?)", (newPhone.manufacturer,newPhone.model,newPhone.price,newPhone.quantity,newPhone.imei,newPhone.warranty))
        conn.commit()
    else:
        update_phone_quantity(conn ,quantity+1,newPhone.imei)

def update_phone_quantity(conn , quantity , manufacturer , model):
    cur = conn.cursor()
    cur.execute(f"UPDATE {conf.PHONE_TABLE} SET quantity = ? WHERE manufacturer = ? AND model = ?" ,(quantity , manufacturer , model))
    conn.commit()

def add_new_sale(conn , newSale):
    cur = conn.cursor()
    quantity = check_phone_exist(conn , newSale.manufacturer,newSale.model)
    discount = newSale.price / get_phone_price(conn,newSale.manufacturer,newSale.model) * 100
    if quantity >= newSale.quantity:
        cur.execute(f"INSERT INTO {conf.SALE_TABLE} VALUES (?,?,?,?,?,?)",(newSale.manufacturer,newSale.model,newSale.price,newSale.quantity,newSale.date_of_purchase,discount))
        conn.commit()
        update_phone_quantity(conn , quantity-newSale.quantity ,newSale.manufacturer,newSale.model)
    else:
        print("Not enough in stock, try later")

def all_phones_in_stock(conn):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {conf.PHONE_TABLE} WHERE quantity > 0")
    rows = cur.fetchall()
    for row in rows:
        print(f"[{row[0]}] Model-{row[1]} , Price-{row[2]} , Quentity-{row[3]}")

def total_amount_of_sale(conn , date , toDate):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {conf.SALE_TABLE} WHERE  date_of_purchase >= ? AND date_of_purchase <= ?",(date,toDate))
    rows = cur.fetchall()
    print(f"Total amount of sale between {date} to {toDate} is {len(rows)}")

#check if the phone exist in DB
#return the quantity(if quentity = 0 the phone not exist)
def check_phone_exist(conn , manufacturer , model):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {conf.PHONE_TABLE}")
    rows = cur.fetchall()
    for row in rows:
        if row[0] == manufacturer and row[1] == model:
            return int(row[3])
    return 0

def get_phone_price(conn,manufacturer,model):
    curr = conn.cursor()
    curr.execute(f"SELECT price FROM {conf.PHONE_TABLE} WHERE manufacturer = ? AND model = ? " , (manufacturer ,model))
    rows = curr.fetchone()
    return rows[0]