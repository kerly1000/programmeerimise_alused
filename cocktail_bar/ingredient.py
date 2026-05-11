"""Class Ingredient."""

class Ingredient:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    def show_info(self):
        """Shows cocktail name and volume."""
        print(f"{self.name}: {self.volume} ml")
