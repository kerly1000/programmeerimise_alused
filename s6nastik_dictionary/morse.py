"""
Morsetähestik on koodikomplekt, kus igale tekstisümbolile vastab pikkadest ja lühikestest
signaalidest koosnev kood (vt. https://et.wikipedia.org/wiki/Morse). Ilmselt on kõigile teada
appikutse "SOS" kood: "... --- ..." ehk kolm lühikest signaali ("S"), kolm pikka ("O") ja taas
kolm lühikest. Lühikesi signaale tähistatakse punktide, pikki aga kriipsudega.

Vajalik on sõnastik, kus on kirjas morse koodid (iga elemendi võtmeks tähistatav sümbol,
väärtuseks koodi järjend punktidest ja kriipsudest). Aja kokkuhoiu mõttes võid kasutada sellist
rida: tahestik = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.",
"h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---",
"p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--",
"x":"-..-", "y":"-.--", "z":"--.."}
Koosta programm, mis programmi käivitamisel tervitab kasutajat nii tavakeeles kui morse koodina,
lubab seejärel kasutajal sisestada sõnu ning teisendab need sümbolhaaval morsetähestikku
(lisades iga sümboli järele tühiku). Sõnastik ei pruugi sisaldada kõikvõimalikke märke, seega
tuleb iga sümboli puhul kontrollida, kas see üldse esineb sõnastikus. Tähe registrit ehk suur-
ja väiketähti ei eristata. Samuti tuleb otsustada, mida ette võtta nende tähtedega, mida
inglise tähestikus pole (näiteks "õ", "ä" jne): ignoreerida või mõned neist teisendada
(näiteks "õ" -> "o" vms).
Programm võiks küsida kasutajalt sõnu kas mingi arv kordi või töötada lõpmatult, kuni
kasutaja sõna ei sisesta, vaid vajutab lihtsalt sisestusklahvile.
"""

dict = {"a":".-", "ä":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.",
"h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "õ":"---",
"ö":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "ü":"..-", "v":"...-", "w":".--",
"x":"-..-", "y":"-.--", "z":"--.."}

def translate_to_morse(text: str) -> str:
    result = ""
    for char in text:
        if char in dict:
            result += dict[char] + " "
        else:
            result += char
    return result

greeting = f"Tere! {dict["t"]} {dict["e"]} {dict["r"]} {dict["e"]}!"
print(greeting)

user_input = input(f" Sisesta sõna, millele soovid vastet morse koodina: ")

if __name__ == '__main__':
    user_input = input(f" Sisesta sõna, millele soovid vastet morse koodina: ")
    print(translate_to_morse(user_input))
    while True:
        message = user_input
        if message == " ":
            break

