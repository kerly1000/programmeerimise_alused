"""
 Tuttavad
a.       Loo järjend 3 nimega
b.       Küsi kasutajalt iga nime kohta kas ta tunneb teda, kui ei tunne lase uus nimi sisestada
c.       Alamprogrammiga asenda jäejendis tundmatu nimi sisestatuga
d.       Kirjuta ekraanile kõik nimed iga üks eraldi reale
"""

name_list = ["Kerly", "Sigrid", "Liisi"]

def replace_name(name_list, index, new_name):
    name_list[index] = new_name

total = ""
for i in range(len(name_list)):
    total += name_list[i]
    answer = input(f"Kas {name_list[i]} on sinu tuttav? (jah/ei): ")

    if answer == "ei":
        new_name = input("Sisesta uus nimi: ")
        replace_name(name_list, i, new_name)


print("\nNimed nimekirjas:")
for name in name_list:
    print(name)

