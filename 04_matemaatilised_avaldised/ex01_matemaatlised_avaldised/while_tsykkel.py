"""
1. Funktsioon saab sisendiks arvu, mis näitab, mitu korda peab sõna "hola" sisalduma funktsiooni väljundis.
Ülesanne tuleks lahendada while tsükliga nii, et iga kord, kui väljundsõnale on liidetud hola, siis count väärtus
väheneb ühe võrra. While tsükkel kestab seni, kuni count väärtus on 0.
2. Selles funktsioonis kasutame juhuslikke arve. Ülesande sõnastus on järgmine:
hakkame koostama sõne, mis koosneb miinusmärkidest (-)
võta üks juhuslik arv (vahemikus 0 kuni 1)
kui see arv on alla teatud piiri (threshold), siis lisame sõnesse ühe miinusmärgi
kui see juhuslik arv on üle piiri või piiriga võrdne, siis lõpetame sõne koostamise ära
Seega, me saame iga kord natuke erineva pikkusega tulemuse.
Juhuslikku arvu saab Pythonis random moodulist funktsiooniga random.random(). See tagastab meile arvu vahemikus
0 kuni 1 (0 on kaasa arvatud, 1 ei ole).
Funktsioon võiks välja näha siis järgmine:
3.
"""


def make_hola_string(count: int) -> str:
    """
    Make hola string.

    print(make_hola_string(3)) => "holaholahola"
    print(make_hola_string(0)) => ""
    """
    result = ""
    i = 0
    while i < count:
        result += "hola"
        i += 1
        return result

def generate_string_with_random_length(threshold: float) -> str:
    """
    Generate a string of "-" until random numbers is below threshold.

    Use random.random() to generate a random float.
    If the random number is below threshold, add "-" to result.
    If the random number is greater or equal to the threshold, finish the loop.

    generate_string_with_random_length(0.9) => "-----" (result can vary)
    generate_string_with_random_length(0.5) => "-" (usually empty or 1 minus)
    """
    result = ""


def ask_user_age(age_limit: int) -> int:
    """
    Ask user age.

    You have to ask the user his/her age using input("What is your age?").
    You have to repeat this process until a correct age is entered.
    The age is correct if:
    - it is numeric (answering "a" is not correct)
    - it is greater or equal to the age_limit
    - it is less or equal to 100

    So, if the user enters a wrong age, the user gets a warning.
    The question is repeated until a correct age is entered.
    The function returns the correct age as int.

    Warning is printed out:
    - non numberic input: Wrong input!
    - age < age_limit: Too young!
    - age > 100: Too old!

    An example (with age_limit 18):
    What is your age? a
    Wrong input!
    What is your age? 10
    Too young!
    What is your age? 101
    Too old!
    What is your age? 21

    (function returns 21)
    """