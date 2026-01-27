"""1.	Küsi kasutajalt 3 arvu
2.	Väikseim arv korruta kahega
3.	Küsi kasutajalt arvude ruute ühest kuni eelmise sammu tulemuseni (Kordus)
4.	Teata kas kasutaja vastas õigesti või valesti
5.	Programmi lõpus näita kasutaja valesti vastatud ruutude õiged tulemused (Järjend)
"""

def square_test(a, a, c) -> int:
    a = int(input("Sisesta esimene arv: "))
    b = int(input("Sisesta teine arv: "))
    c = int(input("Sisesta kolmas arv: "))

    vaikseim = min(a, b, c)
    piir = vaikseim * 2

    print(f"\nVäikseim arv on {vaikseim}, korrutatuna kahega: {piir}\n")

    valed_ruudud = []

    for i in range(1, piir + 1):
        vastus = int(input(f"Mis on arvu {i} ruut? "))
        õige = i ** 2

        if vastus == õige:
            print("Õige!")
        else:
            print("Vale")
            valed_ruudud.append((i, õige))

    print("\nValesti vastatud ruudud:")
    if len(valed_ruudud) == 0:
        print("Kõik vastused olid õiged! ")
    else:
        for arv, ruut in valed_ruudud:
            print(f"{arv}² = {ruut}")

if __name__ == '__main__':
    square_test():




