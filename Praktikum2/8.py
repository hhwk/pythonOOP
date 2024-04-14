class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, quantity):
        self.items.append((item_name, quantity))

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)

    def calculate_total(self):
        total_quantity = sum(item[1] for item in self.items)
        return total_quantity

cart = ShoppingCart()
cart.add_item("Картофель", 100)
cart.add_item("Капуста", 200)
cart.add_item("Апельсин", 150)

print("Товары в корзине:")
for item in cart.items:
    print(item[0], "-", item[1])

total_qty = cart.calculate_total()
print("Общее количество:", total_qty)

cart.remove_item("Апельсин")
print("\nОбновленные товары в корзине после удаления апельсина:")
for item in cart.items:
    print(item[0], "-", item[1])

total_qty = cart.calculate_total()
print("Общее количество:", total_qty)
