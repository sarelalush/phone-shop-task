import io
import sys
from src.PhoneClass import *
from src.SaleClass import *
import src.menu as menu
import unittest

class MenuUnitTest(unittest.TestCase):

    def setUp(self):
        self.phone = '\n'.join(["iphone","sarel","1","2","3","12-10-99"])
        self.update_quantit = '\n'.join(["iphone","sarel","5"])
        self.sale = '\n'.join(['iphone', 'i10', '2300' , '1', '15-11-20'])

    def test_create_phone(self):
        s = io.StringIO(self.phone)
        sys.stdin = s
        res = menu.createPhone()
        p = Phone("iphone", "sarel", "1", "2", "3", "10-10-99")
        self.assertTrue(p.equalPhone(res))

    def test_update_quantity(self):
        s = io.StringIO(self.update_quantit)
        sys.stdin = s
        res = menu.update_quantity()
        self.assertTrue(res[0] == "iphone" and res[1] =="sarel" and res[2] == 5)

    def test_create_Sale(self):
        s = io.StringIO(self.sale)
        sys.stdin = s
        res = menu.create_sale()
        s = Sale('iphone', 'i10', '2300' , '1', '15-11-20')
        self.assertTrue(s.equalSale(res))

    def test_value_not_int(self):
        values1 = '\n'.join(["iphone","sarel","1","2","abc","10-12-99"])
        values2 = '\n'.join(['iphone', 'i10', '2300', '1', '00'])
        s = io.StringIO(values1)
        sys.stdin = s
        with self.assertRaises(ValueError):
            menu.createPhone()

        s = io.StringIO(values1)
        sys.stdin = s
        with self.assertRaises(ValueError):
            menu.create_sale()

    def test_value_not_date(self):
        values1 = '\n'.join(["iphone","sarel","1","2","2","00"])
        values2 = '\n'.join(['iphone', 'i10', '2300' , '1', '00'])
        values3 = '\n'.join(["00","00"])
        s = io.StringIO(values1)
        sys.stdin = s
        with self.assertRaises(ValueError):
            menu.createPhone()

        s = io.StringIO(values2)
        sys.stdin = s
        with self.assertRaises(ValueError):
            menu.create_sale()

        s = io.StringIO(values3)
        sys.stdin = s
        with self.assertRaises(ValueError):
            menu.getDate()


if __name__ == "__main__":
    unittest.main()