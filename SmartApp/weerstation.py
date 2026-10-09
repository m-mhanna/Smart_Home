def fahrenheit(temp_celsius):
    # F = 32 + 1.8 * C
    fahrenheit = 32 + 1.8 * temp_celsius
    return fahrenheit


def gevoelstemperatuur(temp_celsius, windsnelheid, luchtvochtigheid):
    gevoel = temp_celsius - (luchtvochtigheid / 100) * windsnelheid
    return gevoel


def weerrapport(temp_celsius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(temp_celsius, windsnelheid, luchtvochtigheid)

    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gevoel < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif gevoel >= 0 and gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif gevoel >= 0 and gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif gevoel >= 10 and gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"


def weerstation():
    totaal_temp = 0

    for dag in range(1, 8):

        while True:
            temp = input(f"Wat is op dag {dag} de temperatuur:")

            if temp == "":
                print("Bye")
                return

            try:
                temp_celsius = float(temp)
                break
            except ValueError:
                print("Ongeldige invoer, probeer opnieuw.")

        while True:
            wind = input(f"Wat is op dag {dag} de windsnelheid[m/s]: ")

            if wind == "":
                print("Bye")
                return

            try:
                windsnelheid = float(wind)

                if windsnelheid < 0:
                    print("Ongeldig invoer, de windsnelheid kan niet negatief zijn")
                    continue

                break
            except ValueError:
                print("Ongeldige invoer, probeer opnieuw.")

        while True:
            vocht = input(f"Wat is op dag {dag} de vochtigheid[%]: ")

            if vocht == "":
                print("Bye")
                return

            try:
                luchtvochtigheid = int(vocht)

                if 0 <= luchtvochtigheid <= 100:
                    break
                else:
                    print("Voer een geheel getal tussen 0 en 100 in.")

            except ValueError:
                print("Ongeldige invoer, probeer opnieuw.")

        temp_fahrenheit = fahrenheit(temp_celsius)

        totaal_temp += temp_celsius
        gemiddelde_temp = totaal_temp / dag

        print(f"Het is {temp_celsius:.2f}C ({temp_fahrenheit:.2f}F)")
        print(weerrapport(temp_celsius, windsnelheid, luchtvochtigheid))
        print(f"Gem. temp tot nu toe is {gemiddelde_temp:.2f}")
        print("=============================================")
