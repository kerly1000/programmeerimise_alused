"""
1.       Küsi kasutaja vanust ja nime
2.       Tervita kasutajat nime pidi niimitu korda kui mitu aastat ta on täisealine olnud (Kordus)
3.       Kirjuta ekraanile nime lõpust 3 tähte.
"""

age = int(input("Kui vana sa oled? "))
name = input("Mis su nimi on? ")
total = age - 18
for i in range(total):
    print(f"Tere, {name}!")
last_letters = name[-3::1]
print(last_letters)