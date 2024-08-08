class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = {}

    def __str__(self):
        return f"{self.name} ({self.email})"

    def add_to_cart(self, product, quantity):
        if product in self.cart:
            self.cart[product] += quantity
        else:
            self.cart[product] = quantity

    def remove_from_cart(self, product, quantity):
        if product in self.cart:
            self.cart[product] -= quantity
            if self.cart[product] <= 0:
                del self.cart[product]

    def view_cart(self):
        if not self.cart:
            return "Cart is empty."
        cart_contents = "\n".join([f"{product.name}: {quantity}" for product, quantity in self.cart.items()])
        return f"Cart Contents:\n{cart_contents}"
