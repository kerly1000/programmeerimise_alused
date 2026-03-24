"""Klassi ja objekti harjutus. Ülesande eesmärk on luua klass Student.
Klassile tuleb luua konstruktor (__init__ meetod).
Konstruktoris tuleb määrata väljad name ja finished.
Konstruktorisse saab ette anda nime väärtuse (mis tuleb omistada väljale name).
finished väärtus on vaikimisi False.

Loe klasside ja objektide kohta rohkem siit: https://pydoc.pages.taltech.ee/oop/classes.html

Ülesande tulemusena peaks töötama järgmine kood:

student = Student("John")
print(student.name)       # John
print(student.finished)   # False
Järgi, et kood oleks korrektselt kommenteeritud:

faili esimesel real peab olema docstring
klassi definitsiooni järel peab olema docstring
meetodi definitsiooni järel peab olema docstring"""


"""Simple class."""


class Student:
    """Student class."""

    def __init__(self, name, finished=False):
        """Construct a Student instance."""
        self.name = name
        self.finished = finished


if __name__ == '__main__':
    student = Student("John")
    print(student.name)  # John
    print(student.finished)

