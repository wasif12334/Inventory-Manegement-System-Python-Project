class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} - Quantity: {self.quantity}, Price: {self.price}"
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Item '{item.name}' added to inventory.")

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                print(f"Item '{name}' removed from inventory.")
                return
        print(f"Item '{name}' not found in inventory.")

    def view_items(self):
        for item in self.items:
            print(item)

    def search_item(self, name):
        for item in self.items:
            if item.name == name:
                print(item)
                return
        print(f"Item '{name}' not found in inventory.")

    def generate_report(self):
        total_value = 0
        for item in self.items:
            total_value += item.quantity * item.price
        print(f"Total Inventory Value: ${total_value}")
def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Items")
        print("4. Search Item")
        print("5. Generate Report")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            item = Item(name, quantity, price)
            inventory.add_item(item)
        elif choice == 2:
            name = input("Enter item name to remove: ")
            inventory.remove_item(name)
        elif choice == 3:
            inventory.view_items()
        elif choice == 4:
            name = input("Enter item name to search: ")
            inventory.search_item(name)
        elif choice == 5:
            inventory.generate_report()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main();
