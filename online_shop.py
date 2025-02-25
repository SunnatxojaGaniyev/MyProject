import json
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def get_price(self):
        pass

    def __str__(self):
        return f"{self.name} - {self.price} so'm"

class PhysicalProduct(Product):
    def __init__(self, id, name, price, weight):
        self.id = id
        self.name = name
        self.price = price
        self.weight = weight

    def get_price(self):
        return self.price

    def __str__(self):
        return super().__str__() + f" (Og'irlik: {self.weight} kg)"

class DigitalProduct(Product):
    def __init__(self, id, name, price, file_size):
        self.id = id
        self.name = name
        self.price = price
        self.file_size = file_size

    def get_price(self):
        return self.price

    def __str__(self):
        return super().__str__() + f" (Fayl hajmi: {self.file_size} MB)"

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def total(self):
        return sum(item.get_price() for item in self.items)

class Order:
    def __init__(self, user, cart):
        self.user = user
        self.cart = cart

class Payment:
    def process_payment(self, order):
        print(f"To'lov qabul qilindi: {order.cart.total()} so'm")

class Shop:
    def __init__(self):
        self.products = []

    def load_products(self, filename):
        with open(filename) as f:
            products_data = json.load(f)
            for item in products_data:
                if item['type'] == 'physical':
                    product = PhysicalProduct(**item)
                elif item['type'] == 'digital':
                    product = DigitalProduct(**item)
                self.products.append(product)

    def show_products(self):
        for product in self.products:
            print(product)

def main():
    shop = Shop()
    shop.load_products('products.json')
    
    print("Mahsulotlar ro'yxati:")
    shop.show_products()

    username = input("Foydalanuvchi nomi: ")
    password = input("Parol: ")
    user = User(username, password)

    cart = Cart()
    while True:
        product_id = int(input("Mahsulot ID ni kiriting (0 to'xtatish uchun): "))
        if product_id == 0:
            break
        product = next((p for p in shop.products if p.id == product_id), None)
        if product:
            cart.add_item(product)
            print(f"{product.name} savatchaga qo'shildi.")

    order = Order(user, cart)
    payment = Payment()
    payment.process_payment(order)

if __name__ == "__main__":
    main()
