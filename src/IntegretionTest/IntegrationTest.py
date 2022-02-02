import io
import os
import sqlite3
import sys
import src.conf as conf
import pytest
import yaml
from src.app import *


def send_input_to_stdin(values):
    s = io.StringIO(values)
    sys.stdin = s


@pytest.fixture()
def db():
    if os.path.isfile(conf.TEST_NAME):
        print("Database exist, skip create")
        return sqlite3.connect(f'file:{conf.TEST_NAME}?mode=rw', uri=True)
    else:
        conn = sqlite3.connect(conf.TEST_NAME)
        for table in conf.TABLES.values():
            conn.cursor().execute(table)

    with open(r'../db/raw_data.yaml') as file:
        records = yaml.load(file, Loader=yaml.FullLoader)
        for key in records.keys():
            for item in records[key]:
                conn.cursor().execute(
                    f"INSERT INTO {key} VALUES({records[key][item]})"
                )
                conn.commit()
    return conn


"testing cli working flow"


def test_1(db):
    "Select option 1 in menu and insert new Phone"
    send_input_to_stdin('\n'.join(["1", "iphone", "12pro", "1", "2", "3", "12-10-99", "0"]))
    command_line_interface(db)

    "Select option 1 in menu and update the quantity"
    send_input_to_stdin('\n'.join(["2", "iphone", "12pro", "1", "0"]))
    command_line_interface(db)

    "Select option 3 in menu and insert the sale"
    send_input_to_stdin('\n'.join(["3", "iphone", "i10", "2300", "1", "15-11-20", "0"]))
    command_line_interface(db)

    "Select option 4 and will print all the phone in the stock"
    send_input_to_stdin('\n'.join(["4", "0"]))
    command_line_interface(db)

    "Select option 5 and will print all the sale between 20-10-12 to 22-10-12"
    send_input_to_stdin('\n'.join(["5", "20-10-12", "22-10-12", "0"]))
    command_line_interface(db)


# testing quantity after adding phone and sale phone
def test_2(db):
    quantity_before_adding_phone = db_utils.get_quantity(db, "iphone", "12pro")
    "Select option 1 in menu and insert new Phone"
    send_input_to_stdin('\n'.join(["1", "iphone", "12pro", "1", "1", "3", "12-10-99", "0"]))

    command_line_interface(db)
    quantity_before_sale = db_utils.get_quantity(db, "iphone", "12pro")

    send_input_to_stdin('\n'.join(["3", "iphone", "12pro", "2300", "1", "15-11-20", "0"]))
    command_line_interface(db)

    quantity_after_sale = db_utils.get_quantity(db, "iphone", "12pro")

    assert quantity_before_adding_phone != quantity_before_sale
    assert quantity_after_sale == quantity_before_adding_phone


# check if after sale phones the stock updating
def test_3(db):
    #adding 3 phones
    send_input_to_stdin('\n'.join(["1", "abc", "1", "1000", "2", "3", "12-10-99", "0"]))
    command_line_interface(db)
    send_input_to_stdin('\n'.join(["1", "abc", "2", "2000", "2", "3", "12-10-99", "0"]))
    command_line_interface(db)
    send_input_to_stdin('\n'.join(["1", "abc", "3", "2300", "2", "3", "12-10-99", "0"]))
    command_line_interface(db)

    #sale 3 phones
    send_input_to_stdin('\n'.join(["3", "abc", "1", "1000", "2", "15-11-20", "0"]))
    command_line_interface(db)
    send_input_to_stdin('\n'.join(["3", "abc", "2", "2000", "2", "15-11-20", "0"]))
    command_line_interface(db)
    send_input_to_stdin('\n'.join(["3", "abc", "3", "2300", "2", "15-11-20", "0"]))
    command_line_interface(db)
    val1 = db_utils.get_row_phone_data(db, "abc", "1")
    val2 = db_utils.get_row_phone_data(db, "abc", "2")
    val3 = db_utils.get_row_phone_data(db, "abc", "3")

    #check if the quantity equal to 0
    assert val1[3] == 0 and val2[3] == 0 and val3[3] == 0
