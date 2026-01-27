
"""
1.       Küsi kasutaja nime ja vanust
2.       Kui nime pikkus on väiksem kui vanus või vanus on alla 5 siis tervita nime pidi 3 korda (Kordus)
3.       Muidu küsi kolm arvu ja nende summa
4.       Teata kas said õige tulemuse.
"""


name = input("Mis su nimi on? ")
age = int(input("Kui vana sa oled? "))

if len(name) < age or age < 5:
    for i in range(3):
        print(f"Tere, {name}!")
else:
    num_1 = int(input("Sisesta kolm arvu. Esimene: "))
    num_2 = int(input("Teine: "))
    num_3 = int(input("Kolmas: "))

    answer = int(input(f"Sisesta vastus- {num_1}+{num_2}+{num_3}= "))
    right_answer = num_1 + num_2 + num_3
    if answer == right_answer:
        print("Tubli! See on õige vastus!")
    else:
        print(f"Vale vastus! Õige on {right_answer}.")