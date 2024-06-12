from datetime import date
from mycollection import Product
from inventory import Inventory

def display_menu():
    print("\nInventory Management System")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Update Product")
    print("4. Display Inventory")
    print("5. Display Product Details")
    print("6. Exit")

def get_product_details():
    try:
        prefix = input("Enter Product Prefix (e.g., 'P' for perfumes, 'T' for treatments): ")
        product_id = prefix + input("Enter Product ID (e.g., 001 for the first product in this category): ")
        name = input("Enter Product Name: ")
        category = input("Enter Product Category: ")
        brand = input("Enter Product Brand: ")
        quantity = int(input("Enter Product Quantity: "))
        expiry_date_str = input("Enter Expiry Date (YYYY-MM-DD): ")
        expiry_date = date.fromisoformat(expiry_date_str)
        return Product(product_id, name, category, brand, quantity, expiry_date)
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

def main():
    inventory = Inventory()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            product = get_product_details()
            if product:
                try:
                    inventory.add_product(product)
                    print("Product added successfully!")
                except ValueError as e:
                    print(f"Error: {e}")

        elif choice == '2':
            try:
                product_id = input("Enter Product ID to remove: ")
                inventory.remove_product(product_id)
                print("Product removed successfully!")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '3':
            try:
                product_id = input("Enter Product ID to update: ")
                quantity = input("Enter new quantity (leave blank to skip): ")
                expiry_date_str = input("Enter new expiry date (YYYY-MM-DD, leave blank to skip): ")

                quantity = int(quantity) if quantity else None
                expiry_date = date.fromisoformat(expiry_date_str) if expiry_date_str else None

                inventory.update_product(product_id, quantity, expiry_date)
                print("Product updated successfully!")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '4':
            print("\nCurrent Inventory:")
            print(inventory)

        elif choice == '5':
            try:
                product_id = input("Enter Product ID to display: ")
                product = inventory.get_product(product_id)
                print(f"\nDetails of Product ID {product_id}:")
                print(product)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
