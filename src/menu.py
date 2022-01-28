from PhoneClass import *
from SaleClass import *


# create new Phone
def createPhone():
    manufacturer = input("Manufacturer : ")
    model = input("Model : ")
    price = input("Price : ")
    quantity = input("Quantity : ")
    imei = input("IMEI : ")
    warranty = input("Warranty : ")

    return Phone(manufacturer, model, price, quantity, imei, warranty)


def choose_for_update_quantity():
    manufacturer = input("Manufacturer : ")
    model = input("Model : ")
    quantity = input("Quantity : ")
    return manufacturer, model, quantity


def create_new_sale():
    manufacturer = input("Manufacturer : ")
    model = input("Model : ")
    price = input("Price : ")
    quantity = input("Quantity : ")
    date_of_purchase = input("Date : ")
    return Sale(manufacturer, model, price, quantity, date_of_purchase)


def getDate():
    date = input("Start date to search : ")
    to_date = input("End date to search : ")
    return date, to_date


def phone_store_menu():
    print("-----------------------------------------------------")
    print("                    Phone store:                    -")
    print("- Add new phone press 1                             -")
    print("- Update quantity press 2                           -")
    print("- Add new sale press 3                              -")
    print("- Print all phone in the stock press 4              -")
    print("- Print total amount of sales between dates press 5 -")
    print("-----------------------------------------------------")
    return input("Your selection: ")
