class Phone:

    def __init__(self,manufacturer,model,price,quantity,imei,warranty):
        self.manufacturer = manufacturer
        self.model = model
        self.price = price
        self.quantity = quantity
        self.imei = imei
        self.warranty = warranty


    def get_all_data(self):
        return (self.manufacturer,self.model,self.price,self.quantity,self.imei,self.warranty)
