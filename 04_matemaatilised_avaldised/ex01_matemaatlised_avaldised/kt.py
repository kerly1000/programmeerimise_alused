"""Telefoniraamat
1. Peab saama sisestada telefoninumbrit ja nime
2. Samal nimel saab olla ainult 1 nr
3. Peab saama küsida nime järgi numbrit ja vastupidi
        a. kui vastet pole, peab saama lisada
4. Programmi sulgemine ei tohi andmeid kaotaa (peab salvestama)
5. Lisa funktsioon terve raamatu kuvamiseks"""



def phone_book()-> dict:
    name = input("Sisesta nimi: ")
    phone_number = input("Siseata number: ")

if __name__ == '__main__':
    phone_book()





