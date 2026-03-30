"""Koosta programm telefoniraamatu loomiseks.

1.       Peab saama sisestada nime ja telefoni numbrit
2.       Samal nimel võib olla ainult üks telefoni number
3.       Peab saama küsida nime järgi numbrit ja numbri järgi nime
    a.       Kui vastet pole, siis peab võimaldama lisamist
4.       Programmi sulgemine ei tohi andmeid kaotada (tuleb salvestada faili)
5.       Lisa funktsioon terve raamatu kuvamiseks"""


def add_to_phonebook(phonebook) -> dict: # Funktsioon telefoniraamatusse andmete lisamiseks
    name = input("Sisesta nimi: ") # Küsime kasutajalt kontakti nime
    phone_number = input("Sisesta telefoninumber: ") # Küsime kasutajalt kontakti telefoninumbrit
    if name in phonebook: # Kontrollime, kas sisestatud nimi on juba telefoniraamatus
        print("Kontakt on juba olemas.") # Prindime vastuse, et kontakt on juba olemas
    else: # Kui eelmine tingimus ei ole täidetud ja nime ei ole....
        phonebook[name] = phone_number # Lisame uue kontkti

        with open("phonebook.txt", "a") as f: # Avame faili lõppu kirjutamise funktsiooniga või loome faili, kui seda veel pole
            f.write(name +":" + phone_number + "\n") # Lisame faili nime ja telefoninumbri. Reavahetus.

        print("Uus kontakt on loodud.") # Anname kasutajale teada, et kontakt on loodud

def find_phone_number(phonebook) -> dict: # Funktsioon nime järgi telefoninumbri leidmiseks
    name = input("Sisesta nimi: ") # Küsime kasutajalt nime
    with open("phonebook.txt") as f: # Avame faili phonebook
        for row in f: # Otsime ridade kaupa
            n, number = row.strip().split(":") # Eraldame sõned kooloniga ja eemaldame reavahetuse
            if n == name: # Kui nimi oli failis
                print(f"Telefon: {number}") # Anname vastuseks telefoninumbri
                return

        print("Ei leitud") # Anname vastuse, et nime ei ole kontaktide nimekirjas

def number_belonging(phonebook) -> dict: # Funktsioon vastab, kellele kuulub sisestatud number
    phone_number = input("Sisesta telefoninumber: ") # Küsime kasutajalt telefoninumbrit

    with open("phonebook.txt") as f: # Avame faili lugemiseks
        for row in f: # Otsime reakaupa
            name, number = row.strip().split(":") # Eraldame sõned ja eemaldame reavahetuse
            if number == phone_number: # Kui number on leitud
                print(f"Seda numbrit kasutab {name}") # Anname vastuseks numbrile vastava nime
                return
        print("Numbrit ei leitud.") # Anname vastuse, et number puudub nimekirjas


def show_phonebook_content(phonebook) -> dict:
    file = open("phonebook.txt", "r")  # Avame faili lugemisrežiimis
    content = file.read()  # Muutuja content saab väärtuseks kogu faili sisu
    print(content)  # Trükime faili sisu ekraanile

if __name__ == '__main__':
    phonebook = {}







