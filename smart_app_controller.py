def aantal_dagen(inputFile):
    with open(inputFile, "r") as file:
        lines = file.readlines()

    return len(lines) - 1


def auto_bereken(inputFile, outputFile):
    with open(inputFile, "r") as file:
        lines = file.readlines()

    with open(outputFile, "w") as output:

        for regel in lines[1:]:
            delen = regel.split()

            datum = delen[0]
            personen = int(delen[1])
            setpoint = float(delen[2])
            outside = float(delen[3])
            precip = float(delen[4])

            verschil = setpoint - outside

            if verschil >= 20:
                cv = 100
            elif verschil >= 10:
                cv = 50
            else:
                cv = 0

            ventilatie = personen + 1
            if ventilatie > 4:
                ventilatie = 4

            if precip < 3:
                bewatering = True
            else:
                bewatering = False

            output.write(
                f"{datum};{cv};{ventilatie};{bewatering}\n"
            )


def overwrite_settings(outputFile):
    datum = input("Geef een datum: ")
    systeem = input("Kies systeem (1=CV,2=Ventilatie,3=Bewatering): ")
    waarde = input("Nieuwe waarde: ")

    with open(outputFile, "r") as file:
        lines = file.readlines()

    gevonden = False

    for i in range(len(lines)):
        delen = lines[i].strip().split(";")

        if delen[0] == datum:
            gevonden = True

            if systeem == "1":
                waarde = int(waarde)

                if waarde < 0 or waarde > 100:
                    return -3

                delen[1] = str(waarde)

            elif systeem == "2":
                waarde = int(waarde)

                if waarde < 0 or waarde > 4:
                    return -3

                delen[2] = str(waarde)

            elif systeem == "3":

                if waarde == "0":
                    delen[3] = "False"

                elif waarde == "1":
                    delen[3] = "True"

                else:
                    return -3

            else:
                return -3

            lines[i] = ";".join(delen) + "\n"
            break

    if not gevonden:
        return -1

    with open(outputFile, "w") as file:
        file.writelines(lines)

    return 0


def smart_app_controller():

    inputFile = "input.txt"
    outputFile = "output.txt"

    while True:

        print("\nSMART APP CONTROLLER")
        print("1. Aantal dagen")
        print("2. Auto berekenen")
        print("3. Overschrijven")
        print("4. Stoppen")

        keuze = input("Maak een keuze: ")

        if keuze == "1":

            print(
                "Aantal dagen:",
                aantal_dagen(inputFile)
            )

        elif keuze == "2":

            auto_bereken(
                inputFile,
                outputFile
            )

            print("Outputbestand aangemaakt.")

        elif keuze == "3":

            resultaat = overwrite_settings(
                outputFile
            )

            if resultaat == 0:
                print("Aanpassing gelukt.")

            elif resultaat == -1:
                print("Datum niet gevonden.")

            elif resultaat == -3:
                print("Ongeldige invoer.")

        elif keuze == "4":

            print("Bye")
            break

        else:

            print("Ongeldige keuze.")





