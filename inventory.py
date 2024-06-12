from mycollection import Product

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            raise ValueError("Product ID already exists.")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        if product_id not in self.products:
            raise ValueError("Product ID not found.")
        del self.products[product_id]

    def update_product(self, product_id, quantity=None, expiry_date=None):
        if product_id not in self.products:
            raise ValueError("Product ID not found.")
        product = self.products[product_id]
        if quantity is not None:
            product.update_quantity(quantity)
        if expiry_date is not None:
            product.update_expiry_date(expiry_date)

    def get_product(self, product_id):
        if product_id not in self.products:
            raise ValueError("Product ID not found.")
        return self.products[product_id]

    def __str__(self):
        if not self.products:
            return "No products in inventory."
        inventory_str = ""
        for product in self.products.values():
            inventory_str += str(product) + "\n"
        return inventory_str.strip()
