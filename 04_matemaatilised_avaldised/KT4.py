"""
1.       Küsi kasutaja sugu ja vanus
2.       Kasuta eale vastavaid tervitusi nii mehele kui ka naisele.
3.       Korda tervitust ea suurendamisega kuni tervitus vahetub või 10 korda.
"""

gender = input("Kas sa oled mees või naine? ")
age = int(input("Kui vana sa oled? "))

def greeting(gender: str, age: int) -> str:
    if age < 18:
        if gender == "mees":
            return "Tere, noormees!"
        else:
            return "Tere, preili!"
    elif age < 40:
        if gender == "mees":
            return "Tere, härra!"
        else:
            return "Tere, proua!"
    elif age < 50:
        if gender == "mees":
            return "Tere, keskealine härra!"
        else:
            return "Tere, keskealine proua!"
    elif age < 70:
        if gender == "mees":
            return "Tere, härrasmees!"
        else:
            return "Tere, daame!"
    else:
        if gender == "mees":
            return "Tere, vanahärra!"
        else:
            return "Tere, vanaproua!"

current_greeting = greeting(gender, age)

count = 0
while count < 10:
    print(f"{current_greeting}")
    age += 1
    count += 1

    new_greeting = greeting(gender, age)
    if new_greeting != current_greeting:
        break


