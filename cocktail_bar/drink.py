"""Class Drink."""

class Drink:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients or []

    def show_info(self):
        """Shows cocktails name and price."""
        print(f"{self.name} - {self.price:.2f} €")

