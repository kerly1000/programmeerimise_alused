"""Koosta programm, mis küsib kasutajalt nime ja vanust ja väljastab ekraanile nimelise
tervituse koos tekstiga, mis ütleb, kas tegemist on 7-18-aastase inimesega."""
def greet_by_name(name: str) -> str:
    return f"Tere, {name}"

def verify_age(age: int) -> int:
    if age >=7 and age <=18:
        return "Oled 7-18 aastane"
    return "Oled liiga noor või vana"

if __name__ == '__main__':
    name = input("Sisesta oma nimi: ")
    age = int(input("Sisesta oma vanus täisaastas numbriga: "))
    greeting = greet_by_name(name)
    age_text = verify_age(age)
    print(greeting, age_text, sep ="\n")

