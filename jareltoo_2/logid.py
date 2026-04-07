def logs_main_menu():

   while True:
        a = input("Vali toiming ja sisesta vastav number. \n1- kuva kõik logikirjed "
              "\n2- näita tüübi järgi \n3- IP-aadressite statistika "
              "\n4- salvesta raport \n0- välju \nSoovin: ")

        if a == "1":
            with open("server.log", "r", encoding="utf-8") as file:
                for line in file:
                    logs = line.strip().split(";")
                    print(logs)

        elif a == "2":
            search = input("Sisesta filtreeritav tüüp (info/ error/ warning/ critical): ").lower()

            with open("server.log") as file:
                for line in file:
                   logs = line.strip().split(";")

                   date = logs[0]
                   ip.address = logs[1]
                   type = logs[2].lower()
                   code = logs[3]

                   total = 0
                   match_count = 0

                   print("\nValitud kirjed:")

                   for log in logs:
                       total = total + 1

                       if logs["type"] == selected:
                           print(log["time"], "|", log["ip"], "|", log["type"], "|", log["code"])
                           match_count = match_count + 1

                   if total > 0:
                       percent = (match_count / total) * 100
                   else:
                       percent = 0

                   print("\nSelliseid kirjeid:", match_count)
                   print("Protsent kõigist:", round(percent, 2), "%")


if __name__ == '__main__':
    logs_main_menu()

search = input("Sisesta toote nimi: ").lower()

            total_quantity = 0
            total_revenue = 0

            with open("müük.txt", "r", encoding="utf-8") as file:
                for line in file:
                    products = line.strip().split(";")

                    product = products[0].lower()
                    quantity = int(products[2])
                    price = float(products[3])

                    if product == search:
                        total = quantity * price

                        print(f"{line.strip()}, Kokku: {total:.2} €")

                        total_quantity += quantity
                        total_revenue += total

                        print(f"Müüdud kokku {total_quantity} tükki")
                        print(f"Toote müügitulu kokku: {total_revenue:.2} €")

with open("fail.txt") as f:
    for rida in f:
        aeg, ip, tyyP, kood = rida.strip().split(";")

        if tyyP == "ERROR":
            print(rida.strip())

Mitme
tüübi
jaoks:

if tyyP in ["ERROR", "CRITICAL"]:
    print(rida.strip())

total = 0
    match_count = 0

    print("\nValitud kirjed:")

    for log in logs:
        total = total + 1

        if log["type"] == selected:
            print(log["time"], "|", log["ip"], "|", log["type"], "|", log["code"])
            match_count = match_count + 1

    if total > 0:
        percent = (match_count / total) * 100
    else:
        percent = 0

    print("\nSelliseid kirjeid:", match_count)
    print("Protsent kõigist:", round(percent, 2), "%")
