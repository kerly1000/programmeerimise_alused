"""
Encapsulation exercise.
Tuleb luua klass Student ning kasutada "privaatseid" muutujaid. Objekti loomisel (konstruktoris)
võetakse vastu kaks väärtust selles järjekorras: nimi (sõne) ja id (täisarv). Seega peab
konstruktor aktsepteerima kahte parameetrit. Need väärtused salvestatakse "privaatsetesse"
muutujatesse. Lisaks on igal tudengil eraldi info staatuse kohta. Vaikimisi staatus (kui
tudeng luuakse) on "Active".

Tudengi objektil on võimalik muuta nime ja staatust. Id väärtust jooksvalt enam muuta ei saa.
Staatuse muutmisel on kindlad reeglid.

Tudengi objektil peavad olema järgmised meetodid:

get_id(self) - tagastab algselt tudengile määratud id.
set_name(self, name) - määrab tudengile uue nime
get_name(self) - tagastab tudengi hetke nime
set_status(self, status) - määrab tudengile uue staatuse, aga seda vaid juhul, kui staatuse
väärtus on üks järgmistest: Active, Expelled, Finished, Inactive. Muul juhul staatust ei
muudeta (viga ka ei anta - funktsioon lihtsalt ei tee midagi)
get_status(self) - tagastab tudengi hetke staatuse
Kuigi üldiselt on väga hea kasutada "privaatseid" muutujaid oma klassis, siis Pythonis seda
alati ei tehta (teistes keeltes on see rohkem kasutusel). Samas on hea, kui oskad vajadusel
oma muutujaid n-ö ära peita välismaailma eest.
"""
class Student:
    """Represent student with name, id and status."""
    STATUS_ACTIVE = "Active"
    STATUS_EXPELLED = "Expelled"
    STATUS_FINISHED = "Finished"
    STATUS_INACTIVE = "Inactive"

    def __init__(self, name: str, id: int):
        """Initialize student object"""
        self.__name = name
        self.__id = id
        self.__status = Student.STATUS_ACTIVE

    def get_id(self) -> int:
        """Returns student id."""
        return self.__id

    def set_name(self, name) -> None:
        """Set the name of student"""
        self.__name = name

    def get_name(self):
        return self.__name

    def set_status(self, status: str) -> None:
        """Set student status only if given status is correct."""
        allowed_statuses = [Student.STATUS_ACTIVE, Student.STATUS_EXPELLED, Student.STATUS_FINISHED, Student.STATUS_INACTIVE]
        if status in allowed_statuses:
            self.__status = status

    def get_status(self):
        """Get student status"""
        return self.__status

if __name__ == '__main__':
    student1 = Student("Tiit", 1)
    print(student1.get_status())
    student1.set_status("Lahkunud")
    print(student1.get_status())
    student1.set_status("Finished")
    print(student1.get_status())
    student1.set_status(Student.STATUS_ACTIVE)
    print(student1.get_status())

