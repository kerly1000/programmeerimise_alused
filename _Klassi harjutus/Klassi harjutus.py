class House:
    """House class."""

    def __init__(self, rooms, floors, address):
        """House constructor."""
        self.rooms = rooms
        self.floors = floors
        self.address = address

    def show_house_data(self):
        """Show information about house"""
        return f"Aadress: {self.address}, tubade arv: {self.rooms}, korruseid: {self.floors}"

    def renovate_house(self, new_rooms):
        """Show new amount of rooms and value after renovation."""
        if new_rooms <= 0:
            print("Viga: tubade arv ei saa olla 0.")
        else:
            self.rooms = new_rooms
            new_value = new_rooms * 25000 + self.floors * 10000
            print(f"Maja renoveeritud, uus tubade arv: {new_rooms}. Uus väärtus: {new_value}")
            return new_rooms

    def evaluate_house(self):
        """Calculate value of house depending of rooms and floors."""
        house_value = self.rooms * 20000 + self.floors * 10000
        return house_value

class Mansion(House):
    """Mansion class."""


    def __init__(self, rooms, floors, address, value_coefficient):
        """Mansion constructor."""
        super().__init__(rooms, floors, address)
        if value_coefficient <= 0:
            raise ValueError ("Väärtuse koefitsient peab olema positiivne!")

        self.value_coefficient = value_coefficient

    def evaluate_house(self):
        "Calculate price with coefficient."
        base_price = super().evaluate_house()
        mansion_value = int(base_price * self.value_coefficient)
        return mansion_value

if __name__ == '__main__':
    try:
        house = House(5, 2, "Kadaka tee 8")

        print(house.show_house_data())
        print(house.evaluate_house())
        print(house.renovate_house(6))
        print(house.renovate_house(0))

        mansion = Mansion(8, 2, "Merirahu tee 8", 1.2)

        print(mansion.show_house_data())
        print(mansion.evaluate_house())
        print(mansion.renovate_house(9))
        print(mansion.renovate_house(-1))

        buildings = [house, mansion]

        for b in buildings:
            print(f"{type(b).__name__} value:", b.evaluate_house())


    except ValueError as e:
        ("Tekkis viga:", e)

    house = []

    for i in range(60):
        house.append(House(4, 1, "Tallinn"))
        house.append(House(3, 2, "Haapsalu"))
        house.append(House(3, 1, "Tartu"))
        house.append(House(5, 2, "Pärnu"))
        house.append(House(3, 1, "Tallinn"))

    for i in range(40):
        house.append(Mansion(10, 3, "Pirita", 1.5))
        house.append(Mansion(7, 2, "Nõmme", 1.5))
        house.append(Mansion(5, 2, "Kakumäe", 1.5))
        house.append(Mansion(6, 3, "Pärnu", 1.5))
        house.append(Mansion(7, 1, "Tabasalu", 1.5))

    # meetod kõigi peal
    for h in house:
        print(h.show_house_data())

