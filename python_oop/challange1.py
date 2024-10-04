class Product:

    def __init__(self, name , price , quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity 

    def calcValue(self):
        return f"Total value of {self.name}s in store is {self.price*self.quantity} birr."

NewProduct = Product("orange", 15, 4)
print(NewProduct.calcValue())
