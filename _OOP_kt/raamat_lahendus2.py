class Raamat:
    kogus = 0

    def __init__(self, pealkiri, lehekylgi):
        self.pealkiri = pealkiri
        self.lehekylgi = lehekylgi
        Raamat.kogus += 1

    def kuva_info(self):
        return f"{self.pealkiri}, {self.lehekylgi} lk"

    def on_paks(self):
        return self.lehekylgi > 300


class Opik(Raamat):
    def __init__(self, pealkiri, lehekylgi, aine="matemaatika"):
        super().__init__(pealkiri, lehekylgi)
        self.aine = aine

    def aine_info(self):
        return f"See on {self.aine} õpik"


# Katsetamine
r1 = Raamat("Kalevipoeg", 250)
r2 = Opik("Matemaatika 10", 320)

print(r1.kuva_info())
print(r2.kuva_info())
print(r2.aine_info())

print("Raamatuid kokku:", Raamat.kogus)

# Järjend
raamatud = []

for i in range(60):
    raamatud.append(Raamat(f"Raamat {i}", 100 + i))

for i in range(40):
    raamatud.append(Opik(f"Õpik {i}", 200 + i))

# Meetodi kasutamine kõigi peal
paksud = 0

for r in raamatud:
    if r.on_paks():
        paksud += 1

print("Pakse raamatuid:", paksud)