#!/usr/bin/python
import sqlite3
import sys
import src.db_util as db_utils
import src.conf as conf

import menu


def user_choosing_menu(conn):
    while True:
        try:
            choose = menu.phone_store_menu()
            match int(choose):
                case 1:
                    db_utils.add_new_phone(conn, menu.create_phone())
                case 2:
                    manufacturer, model, quantity = menu.update_quantity()
                    db_utils.update_phone_quantity(conn, quantity, manufacturer, model)
                case 3:
                    db_utils.add_new_sale(conn, menu.create_sale())
                case 4:
                    db_utils.all_phones_in_stock(conn)
                case 5:
                    date, to_date = menu.getDate()
                    db_utils.total_amount_of_sale(conn, date, to_date)
                case _:
                    return False

        except ValueError as err:
            print(f"Unexpected {err}")


if __name__ == '__main__':
    connection = None
    try:
        connection = db_utils.create_db()
        db_utils.load_raw_data(connection)
        db_utils.select_all_by_table(connection, conf.PHONE_TABLE)
        db_utils.select_all_by_table(connection, conf.SALE_TABLE)
        user_choosing_menu(connection)
    except sqlite3.Error as e:
        print(f"Error {e.args[0]}")
        sys.exit(1)
    finally:
        if connection:
            connection.close()
