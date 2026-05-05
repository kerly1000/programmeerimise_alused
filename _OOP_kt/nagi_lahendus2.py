class Nagi:
    kogus = 0  # klassimuutuja

    def __init__(self, max_kohad):
        self.max_kohad = max_kohad
        self.riided = []
        Nagi.kogus += 1

    def lisa_riie(self, ese):
        if len(self.riided) >= self.max_kohad:
            print("Nagi on täis!")
        else:
            self.riided.append(ese)

    def eemalda_riie(self, ese):
        if ese in self.riided:
            self.riided.remove(ese)
        else:
            print("Seda eset pole nagis.")

    def kuva(self):
        return f"Nagi sisu: {self.riided}"


class NutikasNagi(Nagi):

    def __init__(self, max_kohad, max_kaal=10):
        super().__init__(max_kohad)
        self.max_kaal = max_kaal

    def lisa_riie(self, ese):
        if ese == "mantel" and len(self.riided) >= self.max_kohad - 1:
            print("Mantel vajab rohkem ruumi!")
        else:
            super().lisa_riie(ese)

if __name__ == "__main__":
    try:
        n1 = Nagi(3)
        n1.lisa_riie("jope")
        n1.lisa_riie("müts")
        print(n1.kuva())

        n2 = NutikasNagi(3)
        n2.lisa_riie("jope")
        n2.lisa_riie("mantel")
        n2.lisa_riie("mantel")
        print(n2.kuva())

    except ValueError:
        print("Tundmatu")

    print("Nagisid kokku:", Nagi.kogus)

    #järjend 100 objektiga
    nagid = []

    for i in range(60):
        nagid.append(Nagi(3))

    for i in range(40):
        nagid.append(NutikasNagi(3))


    #meetod kõigi peal
    for n in nagid[:5]:
        print(n.kuva())

    #kuidas kontrollida, et pärimine töötab
    print(isinstance(n2, Nagi))  # True