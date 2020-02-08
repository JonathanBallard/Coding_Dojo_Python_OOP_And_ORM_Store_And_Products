
class Store:
    def __init__(self, name):
        self.name = name
        self.list_of_products = list()
    def add_product(self, new_product):
        self.list_of_products.append(new_product)
    def sell_product(self, id):
        prod = self.list_of_products.pop(id)
        print('Product:', prod.name, prod.price, prod.category)
    


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def updatePrice(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change
    def print_info(self):
        print('Name', self.name)
        print('Price', self.price)
        print('Category', self.category)





store1 = Store("Store One")
store2 = Store("Store Two")

prod1 = Product("Product One", 34, "Stuff")
prod2 = Product("Product Two", 14, "Stuff")


store1.add_product(prod1)
store1.add_product(prod2)
store1.sell_product(0)












