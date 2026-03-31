"""ÜLESANDE KIRJELDUS:
Kauplus vajab lihtsat programmi müügiandmete analüüsimiseks.

SISENDANDMED:
Fail "müük.txt" sisaldab müügitehinguid formaaadis:
Toode;Kategooria;Kogus;Hind

Näiteks:
Piim;Piimatooted;2;1.50
Leib;Pagaritooted;1;1.20
Juust;Piimatooted;1;3.50

Kus:
- Toode (toote nimi)
- Kategooria
- Kogus (müüdud tükkides)
- Hind (ühiku hind eurodes)

ÜLESANDED:

1. Loe fail sisse ja salvesta tehingud järjendisse (iga tehing on sõnastik).

2. Kuva menüü järgmiste valikutega:
   1 - Kuva kõik tehingud
   2 - Otsi toodet
   3 - Kategooriate analüüs
   4 - Salvesta kokkuvõte
   0 - Välju

3. KUVA KÕIK TEHINGUD: Prindi välja kõik tehingud koos summa arvutusega (kogus * hind).
   Kuva ka kogutulu.

4. OTSI TOODET: Kasutaja sisestab toote nime (case-insensitive).
   - Kuva kõik selle toote tehingud
   - Arvuta kokku müüdud kogus
   - Arvuta kogutulu sellest tootest

5. KATEGOORIATE ANALÜÜS:
   - Grupeeri tehingud kategooriate kaupa
   - Iga kategooria kohta näita:
     * Tehingute arv
     * Kogutulu
   - Leia kõige tulutoovam kategooria

6. SALVESTA KOKKUVÕTE: Loo fail "müük_kokkuvõte.txt", kuhu kirjuta:
   - Tehingute koguarv
   - Kogu müügitulu
   - Erinevate toodete arv
   - Kõige tulutoovam kategooria

7. Programm peab töötama tsüklis kuni kasutaja valib "0 - Välju"
"""
from os import close


def sells_data_main():
    a = input("Palun vali toiming ja sisesta vastav number. \n1- soovin näha kõiki tooteid "
              "\n2- soovin otsida toodet \n3- soovin analüüsida kategoriaid "
              "\n4- soovin salvestada kokkuvõtet \n0- välju Soovin: ")

    if a == "1":
        file = open("müük.txt", "r")
        content = file.read()
        print(content)

    if a == "2":


if __name__ == '__main__':
    sells_data_main()
