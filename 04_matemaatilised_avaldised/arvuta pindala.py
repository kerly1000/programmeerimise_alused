"""Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused
 ning väljastab ekraanile ristküliku ümbermõõdu ja pindala."""


def compute_rectangle():
        lenght = float(input("Sisesta ristküliku pikkus: "))
        width = float(input("Sisesta ristküliku laius: "))
        area = lenght * width
        circumference = 2 * (lenght + width)
        print(f"Ristküliku pindala on {area}")
        print(f"Risküliku ümbermõõt on {circumference}")


if __name__ == '__main__':
    compute_rectangle()