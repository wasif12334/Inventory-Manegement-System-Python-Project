class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

def authenticate_user(username, password):
    users = [
        User("admin", "admin123", "admin"),
        User("customer", "customer123", "customer")
    ]
    for user in users:
        if user.username == username and user.password == password:
            return user.role
    return None

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: {self.price}, Stock: {self.stock_quantity}"

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def edit_product(self, product_id, new_details):
        for product in self.products:
            if product.product_id == product_id:
                product.__dict__.update(new_details)
                return
        print("Product not found.")

    def delete_product(self, product_id):
        self.products = [product for product in self.products if product.product_id != product_id]

    def view_all_products(self):
        for product in self.products:
            print(product)

    def search_products(self, query):
        results = [product for product in self.products if query.lower() in product.name.lower() or query.lower() in product.category.lower()]
        if results:
            for product in results:
                print(product)
        else:
            print("No products found.")

    def filter_by_stock_level(self, threshold):
        results = [product for product in self.products if product.stock_quantity <= threshold]
        if results:
            for product in results:
                print(product)
        else:
            print("No products with low stock.")

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")

    role = authenticate_user(username, password)

    if role:
        print(f"Welcome, {role}!")
        inventory = Inventory()

        while True:
            print("\nInventory Management System")
            print("1. Add Product")
            print("2. Edit Product")
            print("3. Delete Product")
            print("4. View All Products")
            print("5. Search Products")
            print("6. Filter by Stock Level")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                product_id = input("Enter product ID: ")
                name = input("Enter product name: ")
                category = input("Enter product category: ")
                price = float(input("Enter product price: "))
                stock_quantity = int(input("Enter stock quantity: "))
                product = Product(product_id, name, category, price, stock_quantity)
                inventory.add_product(product)
            elif choice == '2':
                product_id = input("Enter product ID to edit: ")
                new_details = {}
                new_details['name'] = input("Enter new name (or press Enter to keep the same): ") or None
                new_details['category'] = input("Enter new category (or press Enter to keep the same): ") or None
                new_details['price'] = float(input("Enter new price (or press Enter to keep the same): ")) or None
                new_details['stock_quantity'] = int(input("Enter new stock quantity (or press Enter to keep the same): ")) or None
                inventory.edit_product(product_id, new_details)
            elif choice == '3':
                product_id = input("Enter product ID to delete: ")
                inventory.delete_product(product_id)
            elif choice == '4':
                inventory.view_all_products()
            elif choice == '5':
                query = input("Enter search query: ")
                inventory.search_products(query)
            elif choice == '6':
                threshold = int(input("Enter stock level threshold: "))
                inventory.filter_by_stock_level(threshold)
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid credentials.")

if __name__ == "__main__":
     main()