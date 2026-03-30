def lisa():
    nimi = input("Nimi: ")
    number = input("Number: ")

    with open("telefon.txt") as f:
        if any(rida.startswith(nimi + ",") for rida in f):
            print("Nimi juba olemas.")
            return

    with open("telefon.txt","a") as f:
        f.write(nimi + "," + number + "\n")


def otsi_nimi():
    nimi = input("Nimi: ")

    with open("telefon.txt") as f:
        for rida in f:
            n, nr = rida.strip().split(",")
            if n == nimi:
                print("Telefon:", nr)
                return
        else:
            print("Ei leitud")


def kuva():
    with open("telefon.txt") as f:
        for rida in f:
            print(rida.strip())


while True:

    print("\n1 Lisa")
    print("2 Otsi nime")
    print("3 Kuva")
    print("4 Välju")

    v = input("Vali: ")

    if v == "1":
        lisa()

    elif v == "2":
        otsi_nimi()

    elif v == "3":
        kuva()

    elif v == "4":
        break