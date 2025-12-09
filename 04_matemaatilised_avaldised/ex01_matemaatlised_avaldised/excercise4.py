"""Eelmise ülesande alusel koostage programm M-Koer (Matemaatiline Koer), millele
antakse samuti ette kaks arvu ja tehtemärk, kuid vastus ei kirjutata mitte arvulisel kujul,
 vaid esitatakse "haukudes". Igaks juhuks: tsükleid pole vaja kasutada, me pole neid veel
 õppinud.

Sisestage esimene arv: 2
Sisestage teine arv: 3
Sisestage tehe: +
Tulemus: auh auh auh auh auh"""

def dog_calculate(num_1: float, num_2: float, operation: str) -> str:
    if operation == "+":
        result = num_1 + num_2
        return f"{round(result) * "auh "}"
    return f"tundmatu tehe: {operation}"

if __name__ == '__main__':

    num_1 = float(input("Sisestage arv: "))
    num_2 = float(input("Sisestage arv: "))
    operation = input("Sisestage tehe: ")
    print(f"Vastus: {dog_calculate(num_1, num_2, operation)}")