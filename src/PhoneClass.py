class Phone:

    def __init__(self, manufacturer, model, price, quantity, imei, warranty):
        self.manufacturer = manufacturer
        self.model = model
        self.price = int(price)
        self.quantity = int(quantity)
        self.imei = int(imei)
        self.warranty = warranty

    def get_all_data(self):
        return self.manufacturer, self.model, self.price, self.quantity, self.imei, self.warranty

    def equal_phone(self, phone):
        if self.manufacturer == phone.manufacturer and self.model == phone.model and self.imei == phone.imei:
            return True
        return False
