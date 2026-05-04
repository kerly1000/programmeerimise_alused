class House:
    def __init__(self, rooms, floors, address):
        if rooms <= 0 or floors <= 0:
            raise ValueError("Tubade ja korruste arv peab olema positiivne.")

        self.rooms = rooms
        self.floors = floors
        self.address = address

    def show_house_data(self):
        return f"Aadress: {self.address}, Toad: {self.rooms}, Korrused: {self.floors}"

    def renovate_house(self, new_rooms):
        if new_rooms <= 0:
            print("Viga: tubade arv peab olema positiivne.")
        else:
            self.rooms = new_rooms
            print("Maja renoveeritud.")

    def evaluate_house(self):
        price = self.rooms * 50000 + self.floors * 30000
        return price


# 🔽 Alamklass
class Mansion(House):
    def __init__(self, rooms, floors, address, value_coefficient):
        super().__init__(rooms, floors, address)

        if value_coefficient <= 0:
            raise ValueError("Koefitsient peab olema positiivne.")

        self.value_coefficient = value_coefficient

    # 🔁 Polümorfism
    def evaluate_house(self):
        base_price = super().evaluate_house()
        mansion_value = int(base_price * self.value_coefficient)
        return mansion_value


# 🔽 Testimine
if __name__ == '__main__':
    try:
        # Tavaline maja
        house = House(2, 1, "Kotka tee 8")

        print(house.show_house_data())
        print("House value:", house.evaluate_house())

        house.renovate_house(4)
        print(house.show_house_data())

        # Veaolukord
        house.renovate_house(-2)

        print("\n---\n")

        # Mõis (alamklass)
        mansion = Mansion(5, 2, "Merirahu tee 8", 2.5)

        print(mansion.show_house_data())
        print("Mansion value:", mansion.evaluate_house())

        print("\n--- Polümorfism ---")

        # Polümorfism demonstratsioon
        buildings = [house, mansion]

        for b in buildings:
            print(f"{type(b).__name__} value:", b.evaluate_house())

    except ValueError as e:
        print("Tekkis viga:", e)