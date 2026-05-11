from drink import Drink


class Mocktail(Drink):

    def __init__(self, name, price, ingredients):
        super().__init__(name, price, ingredients)

    def show_info(self):
        """Shows info about drink details."""
        print(
            f"{self.name} - "
            f"{self.price:.2f}€ - "
            f"Non-alcoholic"
        )