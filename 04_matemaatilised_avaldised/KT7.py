"""
1.       Küsi kasutajalt 1 arv mille paned astmele 2,3,4 ja 5 kasutades kordust ning kuva tulemused ekraanile.
2.       Peale seda küsi kasutajalt kas ta soovib teise arvuga seda teha või lõpetada. (Kordus)
"""

while True:
    number = int(input("Sisesta arv: "))
    print("Arv astendustes:")
    for power in range(2, 6):
        result = number ** power
        print(f"{number}^{power} = {result}")

    to_continue = input("Kas soovid uut numbrit? (jah/ei):")
    if to_continue == "ei":
        print("Lõpetatud!")
        break