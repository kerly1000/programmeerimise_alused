"""1.       Küsi kasutajalt 3 arvu
2.       Väikseim arv korruta kahega
3.       Küsi kasutajalt arvude ruute ühest kuni eelmise sammu tulemuseni (Kordus)
4.       Teata kas kasutaja vastas õigesti või valesti
5.       Teata mitu korda vastas õigesti."""


def squares() -> int:
    num_1 = int(input("Sisesta 3 täisarvu. Esimene: "))
    num_2 = int(input("Teine: "))
    num_3 = int(input("Kolmas: "))

    min_num = min(num_1, num_2, num_3)
    last_value = min_num * 2
    print(f"Väikseim arv on {min_num}, korrutis kahega {last_value}")

    right_answers = 0
    for i in range(1, last_value + 1):
        answer = int(input(f"Kui palju on {i} ruudus? "))
        if answer == i ** 2:
            print("Õige!")
            right_answers += 1
        else:
            print(f"Vale! Õige vastus on {i ** 2}")
    print(f"Sa vastasid õigesti {right_answers} korda!")




if __name__ == '__main__':
    squares()
