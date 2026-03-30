"""Koosta programm, mis "viskab täringut" kolm korda ehk väljastab ekraanile 3
juhusliku täringuviske tulemused. Et ekraanipilt oleks realistlikum, esita tulemused
graafiliselt, selleks kasuta nn. ASCII graafikat (https://en.wikipedia.org/wiki/ASCII_art):
imiteeri tekstisümbolite abil täringu külje kujutist.
Täiendamiseks:
Kasutaja võib alguses ise valida, mitu korda täringut visata.
Mängida võib mitu inimest, programmi alguses küsitakse inimeste nimesid.
Täringut imiteeritakse kolmemõõtmelisena."""

from random import randint

def roll_the_dice() -> tuple[int, str]:
    roll_result = randint(1,6)
    return roll_result

def play_turn(throw_count)

if __name__ == '__main__':
    number_of_throws = int(input("Mitu täringut veeretame? "))
    if number_of_throws.isdigit():
        number_of_throws = int(number_of_throws)
    else:
        number_of_throws = 3
    players_count = input("Mitu mängijat? ")
    if not players_count.isdigit():
        for i in range():
    number = number_of_throws
    total = 0
        for i in range(number):

            total += 1

