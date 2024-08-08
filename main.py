from store import Store
from product import Product
from customer import Customer
from order import Order

def main():
    # Mağaza oluşturma
    store = Store()

    # Ürünler ekleme
    product1 = Product("Laptop", 999.99, 10)
    product2 = Product("Smartphone", 499.99, 20)
    product3 = Product("Headphones", 79.99, 50)
    store.add_product(product1)
    store.add_product(product2)
    store.add_product(product3)

    # Müşteri ekleme
    customer1 = Customer("Alice", "alice@example.com")
    customer2 = Customer("Bob", "bob@example.com")
    store.add_customer(customer1)
    store.add_customer(customer2)

    # Ürünleri listeleme
    print("Available Products:")
    print(store.list_products())

    # Müşterinin sepete ürün eklemesi
    customer1.add_to_cart(product1, 1)
    customer1.add_to_cart(product3, 2)
    print("\nAlice's Cart:")
    print(customer1.view_cart())

    # Sipariş oluşturma
    order1 = Order(customer1)
    print("\nOrder Details:")
    print(order1)

if __name__ == "__main__":
    main()