"""
1.       Küsi kasutajalt arvu.
2.       Kui arv on positiivne, ütle kasutajale, et ta prooviks pigem negatiivset arvu sisestada.
3.       Kui arv on negatiivne, ütle kasutajale, et ta prooviks pigem positiivset arvu sisestada.
4.       Kui arv on 0, õnnitlege kasutajat ja öelge, et olete mängule ära teinud ja pääsete igavesest kordusest.

"""



while True:
    number = int(input("Sisesta number: "))
    if number > 0:
        print("Proovi pigem negatiivset arvu sisestada: ")
    elif number < 0:
        print("Proovi pigem positiivset arvu sisestada: ")
    else:
        print("Palju õnne! Võitsid mängu ja pääsesid igavesest kordusest!")
        break