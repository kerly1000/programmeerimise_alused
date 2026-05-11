"""Class Bar."""
from alcoholic_drink import AlcoholicDrink
from mocktail import Mocktail
from ingredient import Ingredient
from order import Order


class Bar:
    def __init__(self):

        mojito_ingredients = [
            Ingredient("White rum", 50),
            Ingredient("Mint", 10),
            Ingredient("Lime juice", 20)
        ]

        margarita_ingredients = [
            Ingredient("Tequila", 50),
            Ingredient("Triple sec", 20),
            Ingredient("Lime juice", 20)
        ]

        pina_colada_ingredients = [
            Ingredient("White rum", 50),
            Ingredient("Coconut milk", 20),
            Ingredient("Pineapple juice", 50)
        ]

        virgin_mojito_ingredients = [
            Ingredient("Mint", 10),
            Ingredient("Lime juice", 20)
        ]

        self.menu = [
            AlcoholicDrink("Mojito", 7.50, mojito_ingredients, 14),
            AlcoholicDrink("Margarita", 8.50, margarita_ingredients, 18),
            AlcoholicDrink("Pina Colada", 9.00, pina_colada_ingredients, 15),
            Mocktail("Virgin Mojito", 6.50, virgin_mojito_ingredients)
        ]

        self.stock = {
            "White rum": 100,
            "Mint": 100,
            "Lime juice": 200,
            "Tequila": 300,
            "Triple sec": 150,
            "Coconut milk": 200,
            "Pineapple juice": 400
        }

    def show_menu(self):
        """Show cocktails menu."""
        print("\n--- COCKTAIL MENU ---")

        for index, drink in enumerate(self.menu, start=1):
            print(f"{index}. ", end="")
            drink.show_info()

    def check_ingredients(self, drink):
        """Checks ingredients availability in stock."""
        for ingredient in drink.ingredients:

            ingredient_name = ingredient.name
            required_volume = ingredient.volume

            if ingredient_name not in self.stock:
                return False

            if self.stock[ingredient_name] < required_volume:
                return False

        return True

    def use_ingredients(self, drink):
        """Use ingredients from stock."""

        for ingredient in drink.ingredients:
            ingredient_name = ingredient.name
            required_volume = ingredient.volume

            self.stock[ingredient_name] = required_volume

    def bar(self):
        """Run cocktail bar program."""
        print("Welcome to the Cocktail Bar!")

        order = Order()

        while True:
            self.show_menu()

            choice = input("\nChoose a drink or hit q to quit: ")

            if choice.lower() == "q":
                print("See you next time!")
                break

            if choice.lower() == "order":
                order.show_order()
                continue

            if choice.isdigit():
                choice = int(choice)

                if 1 <= choice <= len(self.menu):
                    selected_drink = self.menu[choice - 1]

                    if self.check_ingredients(selected_drink):
                        self.use_ingredients(selected_drink)
                        order.add_drink(selected_drink)

                        print(f"\n{selected_drink.name} added to order!")

                        next_step = input("\nWould you like to add another drink? (yes/finished): ")

                        if next_step.lower() == "finished":
                            order.show_order()
                            print("\nThank you for your order!")
                            break

                        elif next_step.lower() == "yes":
                            continue

                        else:
                            print("Unknown choice. Going to menu.")

                    else:
                        print("\nSorry, not enough ingredients.")

                else:
                    print("Invalid choice.")

            else:
                print("Please enter a number.")
