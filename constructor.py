"""Constructor exercise.
Ülesandes on vaja luua kolm klassi:

Empty - siin konstruktorit pole. Kui jätame konstruktori kirjutamata, siis tegelikult
kasutatakse vaikimisi konstruktorit, mis midagi erilist ei tee. Päriselt kasutatakse seda
väga harva.

Person - siin on konstruktor, mis ei võta ühtegi argumenti sisse. Konstruktoris tuleb luua
objektile väljad: firstname, lastname ja age. Vastavalt vaikeväärtustega: "", "" ja 0.

Student - siin konstruktor võtab vastu 3 argumenti: firstname, lastname ja age. Need
salvestatakse objekti juurde samanimelistesse muutujatesse.

Kirjuta "main" (if __name__ == '__main__' osasse) järgmine kood:

Loo Empty objekt

Loo 3 Person objekti ja määra igale objektile eesnimi, perenimi ja vanus (kõigile erinevad
väärtused)

Loo 3 Student objekti ja määra igale objektile eesnimi, perenimi ja vanus (kõigile erinevad
väärtused)

Kui paned tähele, siis Person objekti puhul peame väärtused eraldi määrama (kuna konstruktoris
pole parameetreid). Student puhul aga saame mugavalt väärtused kaasa anda ja objektide täitmine
andmetega on oluliselt mugavam."""

"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        """Construct class."""
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname, lastname, age):
        """Construct class."""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    # empty usage
    empty_object = Empty()

    p1 = Person()
    p1.firstname = "Tiit"
    p1.lastname = "Sukk"
    p1.age = 35
    p2 = Person()
    p2.firstname = "Kerly"
    p2.lastname = "Ritsu"
    p2.age = 25
    p3 = Person()
    p3.firstname = "Kerly"
    p3.lastname = "Ritsu"
    p3.age = 25
    # 3 x person usage
    s1 = Student("Kerly", "Ritsu", 25)
    s2 = Student("Sigrid", "Sõrmus", 34)
    s3 = Student("Riho", "Sepp", 29)
    # 3 x student usage
