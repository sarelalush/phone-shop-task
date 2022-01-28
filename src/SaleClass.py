class Sale:

    def __init__(self,manufacturer,model,price,quantity,date_of_purchase,discount = 0):
        self.manufacturer = manufacturer
        self.model = model
        self.price = int(price)
        self.quantity = int(quantity)
        self.date_of_purchase = date_of_purchase
        self.discount = discount

    def toString(self):
        return (self.manufacturer,self.model,self.price,self.quantity,self.date_of_purchase,self.discount)
