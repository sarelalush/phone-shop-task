import io
import sys
from src.PhoneClass import *
from src.SaleClass import *
import src.menu as menu
import unittest


def send_input_to_stdin(values):
    s = io.StringIO(values)
    sys.stdin = s


class MenuUnitTest(unittest.TestCase):

    def setUp(self):
        self.phone = '\n'.join(["iphone", "12pro", "1", "2", "3", "12-10-99"])
        self.update_quantity = '\n'.join(["iphone", "12pro", "5"])
        self.sale = '\n'.join(['iphone', 'i10', '2300', '1', '15-11-20'])

    def test_create_phone(self):
        send_input_to_stdin(self.phone)
        res = menu.create_phone()
        p = Phone("iphone", "12pro", "1", "2", "3", "10-10-99")
        self.assertTrue(p.equal_phone(res))

    def test_update_quantity(self):
        send_input_to_stdin(self.update_quantity)
        res = menu.update_quantity()
        self.assertTrue(res[0] == "iphone" and res[1] == "12pro" and res[2] == 5)

    def test_create_Sale(self):
        send_input_to_stdin(self.sale)
        res = menu.create_sale()
        s = Sale('iphone', 'i10', '2300', '1', '15-11-20')
        self.assertTrue(s.get_all_data())

    def test_value_enter_wrong_field(self):
        values1 = '\n'.join(["iphone", "12pro", "1", "2", "abc", "10-12-99"])
        values2 = '\n'.join(['iphone', 'i10', 'avv', '1', '10-12-99'])

        send_input_to_stdin(values1)
        with self.assertRaises(ValueError):
            menu.create_phone()

        send_input_to_stdin(values2)
        with self.assertRaises(ValueError):
            menu.create_sale()

    def test_value_enter_wrong_date(self):
        values1 = '\n'.join(["iphone", "12pro", "1", "2", "2", "00"])
        values2 = '\n'.join(['iphone', 'i10', '2300', '1', '00'])
        values3 = '\n'.join(["00", "00"])

        send_input_to_stdin(values1)
        with self.assertRaises(ValueError):
            menu.create_phone()

        send_input_to_stdin(values2)
        with self.assertRaises(ValueError):
            menu.create_sale()

        send_input_to_stdin(values3)
        with self.assertRaises(ValueError):
            menu.getDate()


if __name__ == "__main__":
    unittest.main()
