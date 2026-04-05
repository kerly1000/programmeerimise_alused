"""Koosta lihtne kalkulaator. Kasutajalt küsitakse kaks arvu ja tehtemärk ning
seejärel kuvatakse tehe koos vastusega
Sisestage esimene arv: 2
Sisestage teine arv: 3
Sisestage tehe: +
Tulemus: 2+3=5"""


def calculate(num_1: float, num_2: float, operation: str) -> str:
    if operation == "+":
        result = num_1 + num_2
        return f"{num_1}+{num_2}={result}"
    return f"tundmatu tehe: {operation}"

if __name__ == '__main__':

    num_1 = float(input("Sisestage arv: "))
    num_2 = float(input("Sisestage arv: "))
    operation = input("Sisestage tehe: ")
    print(f"Vastus: {calculate(num_1, num_2, operation)}")

