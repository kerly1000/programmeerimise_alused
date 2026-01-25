"""
1.       Kasutajalt küsitakse sõna.
2.       Kasutajalt küsitakse numbrit.
3.       Konsool prindib antud sõna välja sisestatud number * 2 korda (kordus).
4.       Juhul kui sisestatud number on suurem kui 10, tagastatakse „Viga“.
"""

word = input("Sisesta 1 sõna: ")
number = int(input("Sisesta üks number: "))
if number < 10:
    total = number * 2
    i = word
    for i in range(total):
        print(f"{word}")

