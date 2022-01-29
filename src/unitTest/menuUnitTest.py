import io
import sys
from src.PhoneClass import *
import src.menu as menu
import unittest

class MenuUnitTest(unittest.TestCase):

    def setUp(self):
        self.phone = '\n'.join(["iphone","sarel","1","2","3","20-20-1999"])
        self.update_quantit = '\n'.join(["iphone","sarel","5"])

    def test_create_phone(self):
        s = io.StringIO(self.phone)
        sys.stdin = s
        res = menu.createPhone()
        p = Phone("iphone", "sarel", "1", "2", "3", "20-20-1999")
        self.assertTrue(p.equalPhone(res))

    def test_update_quantity(self):
        s = io.StringIO(self.update_quantit)
        sys.stdin = s
        res = menu.update_quantity()
        self.assertTrue(res[0] == "iphone" and res[1] =="sarel" and res[2] == 5)


if __name__ == "__main__":
    unittest.main()