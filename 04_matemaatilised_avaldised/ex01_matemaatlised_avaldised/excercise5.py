"""Koosta programm, mis küsib kasutajalt temperatuuri Celsiuse kraadides ja väljastab
 tulemuse Fahrenheiti kraadides. Kuidas muuta programmi nii, et võimalik oleks teisendamine
  nii üht- kui teistpidi? Proovi."""


def convert_to_farenheit(celsius_temperature: float) -> float:

    return temperature_celsius * 1.8 + 32

def convert_to_celsius(farenheit_temperature: float) -> float:

    return (temperature_farenheit - 32) / 1.8

if __name__ == '__main__':
    unit = input("Määra sisestatava temperatuuri ühik (C/F): ")
    if unit.upper() == "C":
        temperature_celsius = float(input("Sisesta temperatuuri Celsiuse kraadides: "))
        temperature_farenheit = convert_to_farenheit(temperature_celsius)
        print(f"{temperature_celsius}C on {temperature_farenheit:.2f}F kraadi")
    elif unit.upper() == "F":
        temperature_farenheit = float(input("Sisesta temperatuuri Farenheit kraadides: "))
        temperature_celsius = convert_to_celsius(temperature_farenheit)
        print(f"{temperature_farenheit}F on {temperature_celsius:.2f}C kraadi")
    else:
        print(f"Sisestasid tundmatu temperatuuriühiku - {unit}")
        print("Programm toetab C- Celsius ja F - Farenheit kraade")