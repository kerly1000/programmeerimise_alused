"""
Koosta mäng, kus saate ära arvata arvuti poolt mõeldud täisarvu ühest kahekümneni. nt:
Mõtlesin ühele täisarvule 1-20ni. Mis arv see on?
>> 15
Liiga suur, proovi uuesti.
>> 7
Liiga väike, proovi uuesti.
>> 9
Liiga väike, proovi uuesti.
>> 11
Tubli, arvasid ära. Arv oli 11.
Enne ülesande lahendamist mõelge välja mängu algoritm ja koostage selle kohta plokkskeem.
1. jäta meelde suvaline arv 1-20
2. korda
    küsi kasutajalt arvu
        ütle, kas suurem
        ütle, kas väiksem
        ütle õige ja lõpeta
"""
from random import randint

def play_guessing_game():
    correct = randint (1, 20)
    tries = 0
    while tries < 5:
            answer = int(input("Sisesta arv vahemikus 1-20: "))
            tries += 1
            if answer > correct:
                print("Liiga suur, proovi uuesti!")
                continue
            if answer < correct:
                print("Liiga väike, proovi uuesti!")
                continue
            print(f"Tubli! Arvasid ära. Arv oli {correct}")
            break
    else:
        print(f"Katsed said otsa. Mõtlesin arvule {correct}")

if __name__ == '__main__':
    play_guessing_game()



