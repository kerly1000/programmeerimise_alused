"""1.       Küsi kasutajalt 3 arvu
2.       Väikseim arv korruta kahega
3.       Küsi kasutajalt arvude ruute ühest kuni eelmise sammu tulemuseni (Kordus)
4.       Teata kas kasutaja vastas õigesti või valesti
5.       Teata mitu korda kasutaja vastas õigesti."""


def squares() -> int:
    num_1 = int(input("Sisesta 3 täisarvu. Esimene: "))
    num_2 = int(input("Teine: "))
    num_3 = int(input("Kolmas: "))

    minimum = min([num_1, num_2, num_3])

    square_calc = minimum ** 2

    print(f"Kui palju on 1 ruudus?: ")


if __name__ == '__main__':
    squares()

