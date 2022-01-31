import io
import os
import sys

from src.PhoneClass import *
from src.SaleClass import *
import src.db_util as db_utils
import sqlite3
import src.conf as conf
import pytest
import yaml


@pytest.fixture()
def db():
    if os.path.isfile(conf.TEST_NAME):
        print("Database exist, skip create")
        return sqlite3.connect(f'file:{conf.TEST_NAME}?mode=rw', uri=True)
    else:
        conn = sqlite3.connect(conf.TEST_NAME)
        for table in conf.TABLES.values():
            conn.cursor().execute(table)

    with open(r'raw_data.yaml') as file:
        records = yaml.load(file, Loader=yaml.FullLoader)
        for key in records.keys():
            for item in records[key]:
                conn.cursor().execute(
                    f"INSERT INTO {key} VALUES({records[key][item]})"
                )
                conn.commit()
    return conn


def test_add_phone_to_db(db):
    # add the phone to db
    phone = Phone("iphone", "13-ProMax", 1, 2, 3, "20-02-22")
    db_utils.add_new_phone(db, phone)

    # read the phone from db and test it
    c = db_utils.get_row_phone_data(db, phone.manufacturer, phone.model)
    count = db_utils.get_quantity(db, phone.manufacturer, phone.model)
    assert list(c) == ["iphone", "13-ProMax", 1, count, 3, "20-02-22"]


def test_add_sale_to_db(db):
    # add the phone to db
    phone = Phone("iphone", "10_pro", 1, 1, 3, "20-02-22")
    db_utils.add_new_phone(db, phone)

    # add the sale to db
    sale = Sale('iphone', '10_pro', 1150, 1, '11-10-20')
    db_utils.add_new_sale(db, sale)

    # read the sale from db and test it
    c = db_utils.get_row_sale_data(db, sale.manufacturer, sale.model)

    assert ('iphone', '10_pro', 1150, 1, '11-10-20', float(50)) in list(c)


def test_update_quantity_db(db):
    # add 13-ProMax to stock
    phone = Phone("iphone", "10_pro", 1, 2, 3, "20-02-22")
    db_utils.add_new_phone(db, phone)
    # save the quantity before sale
    quantity_before_sale = db_utils.get_quantity(db, 'iphone', '10_pro')
    # add the sale to db
    sale = Sale('iphone', '10_pro', 1150, 2, '15-11-2022')
    db_utils.add_new_sale(db, sale)
    # save the quantity after sale
    quantity_after_sale = db_utils.get_quantity(db, 'iphone', '10_pro')

    assert quantity_before_sale - 2 == quantity_after_sale


def test_total_amount_of_sale_db(db):
    phone = Phone("iphone", "10_pro", 1, 2, 3, "20-02-22")
    db_utils.add_new_phone(db, phone)

    count_before = db_utils.total_amount_of_sale(db, "20-10-10", "20-10-11")
    sale = Sale('iphone', '10_pro', 1150, 2, "20-10-11")

    db_utils.add_new_sale(db, sale)
    count_after = db_utils.total_amount_of_sale(db, "20-10-10", "20-10-11")
    assert count_before == count_after - 1
