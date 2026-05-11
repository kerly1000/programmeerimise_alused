"""Class Order."""

class Order:
    def __init__(self):
        self.drinks = []

    def add_drink(self, drink):
        """Adds drink to order."""
        self.drinks.append(drink)

    def get_total_price(self):
        """Shows total amount of ordered drinks."""
        total = 0

        for drink in self.drinks:
            total += drink.price

        return total

    def show_order(self):
        """Shows order details."""
        if not self.drinks:
            print("No drinks ordered.")
            return

        print("\n--- YOUR ORDER --- ")

        for index, drink in enumerate(self.drinks, start=1):
            print(f"{index}. {drink.name} - {drink.price:.2f} €")

        print(f"Total: {self.get_total_price():.2f} €")
