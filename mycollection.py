from datetime import date

class Product:
    def __init__(self, product_id, name, category, brand, quantity, expiry_date):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.brand = brand
        self.quantity = quantity
        self.expiry_date = expiry_date

    def update_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity

    def update_expiry_date(self, expiry_date):
        self.expiry_date = expiry_date

    def __str__(self):
        return (f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, "
                f"Brand: {self.brand}, Quantity: {self.quantity}, "
                f"Expiry Date: {self.expiry_date}")
