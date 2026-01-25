"""
On traditsioon, et rõõmsatel puhkudel kingitakse paaritu arv lilli. Lillepoel on sünnipäev ja pood otsustas klientidele
kinkida lilli nii, et päeva esimene ostja saab ühe lille, teine ei saa ühtegi, kolmas ostja saab kolm lille, neljas ei
saa midagi, viies ostja saab viis lille jne.
Koostada programm, mis
•küsib kasutajalt klientide arvu (mittenegatiivne täisarv);
•arvutab while-tsükli abil lillede koguarvu, mida pood kingib;
•väljastab saadud lillede arvu ekraanile.
Vihje: lillede koguarvust võib mõelda kui summast, milles liidetavad on paaritud arvud alates 1 kuni esimese paaritu
arvuni, mis pole suurem kui klientide arv.
Näiteks, kui kasutaja sisestas 7, siis paaritute arvude summa on 16, sest 1 + 3 + 5 + 7 = 16.
Kui kasutaja sisestas 8, siis on summaks samuti 16, sest 1 + 3 + 5 + 7 = 16.
"""


visitors = int(input("Mitu klienti käis? "))
amount_of_flowers = 0
current = 1 # esimene paaritu arv

while current <= visitors:
    amount_of_flowers += current
    current += 2 # järgmine paaritu arv

print(f"Lillepood kinkis klientidele {amount_of_flowers} lille.")