""VARIANT 5 (LÜHIKE): SERVERI LOGIFAILIDE ANALÜÜS

ÜLESANDE KIRJELDUS:
Veebiserver vajab lihtsat programmi logifailide analüüsimiseks.

SISENDANDMED:
Fail "server.log" sisaldab serverilogi kirjeid formaaadis:
Aeg;IP-aadress;Tüüp;Kood

Näiteks:
2024-01-15 10:23:45;192.168.1.100;INFO;200
2024-01-15 10:24:12;192.168.1.105;ERROR;500
2024-01-15 10:25:03;192.168.1.100;WARNING;404

Kus:
- Aeg (AAAA-KK-PP HH:MM:SS)
- IP-aadress
- Tüüp (INFO, WARNING, ERROR, CRITICAL)
- Kood (HTTP vastuse kood)

ÜLESANDED:

1. Loe logifail sisse ja salvesta kirjed järjendisse (iga kirje on sõnastik).

2. Kuva menüü järgmiste valikutega:
   1 - Kuva kõik logikirjed
   2 - Filtreeri tüübi järgi
   3 - IP-aadresside statistika
   4 - Salvesta raport
   0 - Välju

3. KUVA KÕIK LOGIKIRJED: Prindi välja kõik kirjed tabelina.
   Kuva ka kokkuvõte: kokku kirjeid, INFO, WARNING, ERROR, CRITICAL arv.

4. FILTREERI TÜÜBI JÄRGI: Kasutaja valib tüübi (INFO/WARNING/ERROR/CRITICAL).
   Kuva kõik selle tüübiga kirjed.
   Kuva ka protsent kõigist kirjetest.

5. IP-AADRESSIDE STATISTIKA:
   - Loe kokku iga IP-aadressi kirjete arv
   - Kuva TOP 5 aktiivsemat IP-aadressi
   - Iga IP kohta näita ka ERROR/CRITICAL kirjete arv

6. SALVESTA RAPORT: Loo fail "server_raport.txt", kuhu kirjuta:
   - Kogu kirjete arv
   - Kirjete jaotus tüüpide järgi (arv ja %)
   - TOP 3 aktiivsemat IP-aadressi
   - Süsteemi staatus (OK kui < 10% vead, muidu HOIATUS)

7. Programm peab töötama tsüklis kuni kasutaja valib "0 - Välju"
"""

