from drink import Drink


class AlcoholicDrink(Drink):

    def __init__(self, name, price, ingredients, alcohol_percentage):
        super().__init__(name, price, ingredients)

        self.alcohol_percentage = alcohol_percentage

    def show_info(self):
        """Shows info about drink details."""
        print(
            f"{self.name} - "
            f"{self.price:.2f}€ - "
            f"{self.alcohol_percentage}% alcohol"
        )