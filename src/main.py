#!/usr/bin/python
import sqlite3
import sys
import src.db_util as db_utils
import src.conf as conf
from app import *



if __name__ == '__main__':
    connection = None
    try:
        connection = db_utils.create_db()
        #db_utils.load_raw_data(connection)
        #db_utils.select_all_by_table(connection, conf.PHONE_TABLE)
        #db_utils.select_all_by_table(connection, conf.SALE_TABLE)
        command_line_interface(connection)
    except sqlite3.Error as e:
        print(f"Error {e.args[0]}")
        sys.exit(1)
    finally:
        if connection:
            connection.close()
