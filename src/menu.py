from src.PhoneClass import *
from src.SaleClass import *
from datetime import datetime

# Fill the fields for new sale and create new phone object
def createPhone():
    manufacturer = input("Manufacturer : ")
    model = input("Model : ")
    price = int(input("Price : "))
    quantity = int(input("Quantity : "))
    imei = int(input("IMEI : "))

    try:
        warranty = input("Warranty : ")
        datetime.strptime(warranty, "%d-%m-%y")
    except ValueError:
        raise ValueError("Incorrect data format, should be DD-MM-YYYY")

    return Phone(manufacturer, model, price, quantity, imei, warranty)


# Fill the fields for quantity
def update_quantity():
    manufacturer = input("Manufacturer : ")
    model = input("Model : ")
    quantity = int(input("Quantity : "))
    return manufacturer, model, quantity


# Fill the fields for new sale and create new sale object
def create_sale():
    manufacturer = input("Manufacturer : ")
    model = input("Model : ")
    price = int(input("Price : "))
    quantity = int(input("Quantity : "))

    try:
        date_of_purchase = input("Date :")
        datetime.strptime(date_of_purchase, "%d-%m-%y")
    except ValueError:
        raise ValueError("Incorrect data format, should be DD-MM-YY")

    return Sale(manufacturer, model, price, quantity, date_of_purchase)


# Fill the fields for sale serach in DB from date to date
def getDate():
    try:
        date = input("Start date to search : ")
        to_date = input("End date to search : ")
        datetime.strptime(date,"%d-%m-%y")
        datetime.strptime(to_date, "%d-%m-%y")
    except ValueError:
        raise ValueError("Incorrect data format, should be DD-MM-YYYY")
    return date, to_date


# The options in menu
def phone_store_menu():
    print("-----------------------------------------------------")
    print("-                   Phone store:                    -")
    print("- Add new phone press 1                             -")
    print("- Update quantity press 2                           -")
    print("- Add new sale press 3                              -")
    print("- Print all phone in the stock press 4              -")
    print("- Print total amount of sales between dates press 5 -")
    print("-----------------------------------------------------")
    user_selection = 0
    try:
        user_selection = int(input("Your selection: "))
    except ValueError as err:
        raise ValueError("Incorrect format, should be Integer")

    return user_selection