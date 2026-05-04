class House:
    """House class."""

    def __init__(self, rooms, floors, address):
        """House constructor."""
        self.rooms = rooms
        self.floors = floors
        self.address = address

    def show_house_data(self):
        """Print info of the given house."""
        print(f"Address: {self.address}")
        print(f"Rooms: {self.rooms}")
        print(f"Floors: {self.floors}")

    def evaluate_house(self):
        """Evaluate price of the house."""
        # Simple base price calculation
        if self.rooms <= 0 or self.floors <= 0:
            raise ValueError("Invalid house data for valuation.")
        house_value = (self.rooms * 10000) + (self.floors * 5000)
        print(f"House value is: {house_value}")
        return house_value



    def renovate_house(self, new_rooms):
        """Calculate new value after renovation."""
        if new_rooms <= 0:
            raise ValueError("Number of rooms must be greater than 0.")
        print(f"Renovating house at {self.address}...")
        self.rooms = new_rooms
        new_value = (new_rooms * 10000) + (self.floors * 5000)
        print(f"Renovation completed. New value is: {new_value}")
        return new_value




class Mansion(House):
    """Mansion class."""

    def __init__(self, rooms, floors, address, value_coefficient):
        """Mansion class constructor."""

        super().__init__(rooms, floors, address)
        self.value_coefficient = value_coefficient

    # Polymorphism: overridden method
    def evaluate_house(self):
        """Evaluate price of the given house."""

        base_price = super().evaluate_house()
        mansion_value =  int(base_price * self.value_coefficient)
        print(f"Mansion value is: {mansion_value}")
        return mansion_value

    def renovate_house(self, new_rooms):
        new_value = self.value_coefficient * ((new_rooms * 10000) + (self.floors * 5000))
        return new_value

if __name__ == '__main__':
    try:
        house = House(2, 1, "Kotka tee 8")

        # Print house info
        house.show_house_data()
        house.evaluate_house()

        house.renovate_house(4)
        house.show_house_data()
        print()

        mansion = Mansion(5, 2, "Merirahu tee 8", 2.5)

        mansion.show_house_data()
        mansion.evaluate_house()

        # Renovation
        mansion.renovate_house(6)
        print()

        # Polymorphism
        buildings = [house, mansion]
        for b in buildings:
            print(f"{type(b).__name__} value:", b.evaluate_house())

        # Error example (uncomment to test)
        # house.renovate_house(-2)

    except ValueError as e:
        print("Error:", e)