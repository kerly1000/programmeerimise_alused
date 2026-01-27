"""
1.       Küsi kasutaja nime
2.       Kui nimepikkus on vahemikus 5 – 10 (kaasa arvatud), siis tervita 3 korda
3.       Muidu küsi kolm arvu ja tagasta nende summa. (Kordus)
"""

name = str(input("Mis su nimi on? "))
if len(name) > 4 < 11:
    for i in range(3):
        print(f"Tere, {name}!")
else:
    num_1 = int(input("Sisesta kolm arvu! Esimene: "))
    num_2 = int(input("Teine: "))
    num_3 = int(input("Kolmas: "))
    total = num_1 + num_2 + num_3
    print(F"Sisestatud arvude summa on {total}." )


