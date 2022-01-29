from src.PhoneClass import *
from src.SaleClass import *
import src.menu as menu
import unittest
import src.db_util as db_utils
import sqlite3
import sys
import src.conf as conf

class DBUnitTest(unittest.TestCase):

    def setUp(self):
        try:
            self.connection = db_utils.create_db()
            db_utils.load_raw_data(self.connection)
        except sqlite3.Error as e:
            print(f"Error {e.args[0]}")
            sys.exit(1)

    def tearDown(self):
        if self.connection:
            self.connection.close()

