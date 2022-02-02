
import src.db_util as db_utils
import src.menu as menu


def command_line_interface(conn):
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

            print("Your selection was made successfully")

        except ValueError as err:
            print(f"Unexpected {err}")