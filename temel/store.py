from product import Product
from customer import Customer
from order import Order

class Store:
    def __init__(self):
        self.products = []
        self.customers = []

    def add_product(self, product):
        self.products.append(product)

    def add_customer(self, customer):
        self.customers.append(customer)

    def list_products(self):
        return "\n".join([str(product) for product in self.products])

    def find_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        return None