class Raamat:
    kogus = 0

    def __init__(self, pealkiri, lehed):
        self.pealkiri = pealkiri
        self.lehed = lehed
        Raamat.kogus += 1

    def kirjeldus(self):
        return f"{self.pealkiri} ({self.lehed} lk)"

    def on_paks(self):
        return self.lehed > 300


class Opik(Raamat):
    def __init__(self, pealkiri, lehed, aine="matemaatika"):
        super().__init__(pealkiri, lehed)
        self.aine = aine

    # 🔁 override (polümorfism)
    def kirjeldus(self):
        return f"{self.pealkiri} - {self.aine} õpik ({self.lehed} lk)"


# 🔽 Katsetamine
raamatud = []

# 60 tavalist
for i in range(60):
    raamatud.append(Raamat(f"R{i}", 100 + i))

# 40 õpikut
for i in range(40):
    raamatud.append(Opik(f"O{i}", 200 + i))

# 🔁 kasutame meetodit kõigi peal (polümorfism)
for r in raamatud[:5]:  # ainult 5 tk, et output ei oleks liiga pikk
    print(r.kirjeldus())

print("Kokku objekte:", Raamat.kogus)

# kasutame teist meetodit kõigi peal
paksud = sum(1 for r in raamatud if r.on_paks())
print("Pakke:", paksud)
