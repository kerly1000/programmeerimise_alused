"""
Koosta programm, mis küsib kasutajalt arvu N ja väljastab O-tähtedest koosneva ruudu suuruses NxN. Seejärel muutke
programmi nii, et ruudu diagonaalidel olevad märgid oleksid X-d, näiteks:

X O O O O O O O X
O X O O O O O X O
O O X O O O X O O
O O O X O X O O O
O O O O X O O O O
O O O X O X O O O
O O X O O O X O O
O X O O O O O X O
X O O O O O O O X
... või (paarisarvulise N-i puhul):

X O O O O O O O O X
O X O O O O O O X O
O O X O O O O X O O
O O O X O O X O O O
O O O O X X O O O O
O O O O X X O O O O
O O O X O O X O O O
O O X O O O O X O O
O X O O O O O O X O
X O O O O O O O O X
Tühikuid võid lisada vastavalt oma soovile.
"""

def square_from_o(size: int, symbol: str, alt: str):
      for row in range(size):
        for col in range(size):
            #print(f"{symbol}", end = " ")
            if row == col or row + col == size - 1:
                print(f"{alt}", end= " ")
            else:
                print(f"{symbol}", end=" ")
        print()


if __name__ == '__main__':
    size = int(input("Kui suure ruudu teeme? "))
    square_from_o(size, "o", "x")

