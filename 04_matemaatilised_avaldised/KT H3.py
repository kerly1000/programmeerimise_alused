"""
On traditsioon, et rõõmsatel puhkudel kingitakse paaritu arv lilli. Üks teine lillepood on otsustanud, et nende
sünnipäeval saab iga klient kingituseks lilli nii, et esimene ostja saab ühe lille, teine ostja saab kolm lille, kolmas
ostja saab viis lille, neljas ostja seitse lille jne.
Koostada programm, mis
•küsib kasutajalt klientide arvu (mittenegatiivne täisarv);
•arvutab while-tsükli abil lillede koguarvu, mida pood klientidele kingib;
•väljastab kingitavate lillede koguarvu.
Näiteks, kui kasutaja sisestas 4, siis paaritute arvude summa on 16, sest 1 + 3 + 5 + 7 = 16.
Kui kasutaja sisestas 7, siis on summaks 49, sest 1 + 3 + 5 + 7 + 9 + 11 + 13 = 49.
"""

visitors = int(input("Mitu klienti poodi külastas? "))
count = 0
current = 1
amount_of_flowers = 0

while count < visitors:
    amount_of_flowers += current
    current += 2
    count += 1
print(f"Lillepood kinkis {amount_of_flowers} lille.")