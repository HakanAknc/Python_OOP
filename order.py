class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = customer.cart.copy()
        self.total = self.calculate_total()

    def __str__(self):
        order_details = "\n".join([f"{product.name}: {quantity}" for product, quantity in self.items.items()])
        return f"Order for {self.customer.name}:\n{order_details}\nTotal: ${self.total}"

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.items.items())