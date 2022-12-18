__author__ = "Adrian Egelandsdal Skeie"

__version__ = "1.0.0"
__email__ = "adrian.skeie.e@gmail.com"
__status__ = "Ferdig"

# Alle biblotek importeringene til programmet
from libraries.filehandling import get_data, update_data
from libraries.interface import *
from libraries.platelibrary import plate_add, clear, remove_plate, plate_quickadd, find_plates, random_plate
from libraries.classes import PlateObject, Colors
from random import choices

# Definerer nødvendige variabler som brukes i programmet.
FILEPATH_PLATES = "libraries/data/platelist.json"
FILEPATH_LENGTHS = "libraries/data/max_lengths.json"

# Definerer noen konstanter som brukes i ID generering
ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"

# Henter data fra json filene i './libraries/data/' til variablene under
plates: list[str] = get_data(FILEPATH_PLATES)
length_formatting: list[int] = get_data(FILEPATH_LENGTHS)


# Egendefinert exception til å hoppe til starten av programmet
class Restart(Exception):
    pass


# Ordbok som inneholder ulike kommandoer som kan bli brukt.
commands = {
    "help": (
        print_commands,
        "Viser denne menyen"
    ),
    "list": (
        print_list,
        "Skriver ut listen med plater"
    ),
    "random": (
        random_plate,
        "Skriver ut en tilfeldig plate som du kan høre på"
    ),
    "find": (
        find_plates,
        "Brukes til å finne spesifikke plater: find -ar [Artist] | -al [Album] | -ps [Plateselskap] | -id [ID]"
    ),
    "addplate": (
        plate_add,
        "Brukes til å lage og legge til en ny plate i 'platelist.json'"
    ),
    "quickadd": (
        plate_quickadd,
        "Gjør det samme som 'nyplate, men går gjennom innleggings prosessen raskere"
    ),
    "clear": (
        clear,
        "Fjerner synlig tekst fra konsollen"
    ),
    "remove": (
        remove_plate,
        "For å fjerne en plate skriver du 'remove [ID]'. "
        "Hvor 'ID' er ID'en til platen når du er på venstre side av plate listen."
    ),
    "exit": (
        exit,
        "Avslutter programmet"
    )
}


def main():
    """ Hovudfunksjonen i programmet hvor alt blir håndtert
    """

    def save_plate(plate):
        """ Nestet funksjon som brukes til å lagre et plateobjekt til 'platelist.json'

        :param plate: En liste med nødvendige element for å bruke klassen PlateObjekt i './libraries/classes.py'
        """

        # Sjekker om 'plate' er en liste
        if isinstance(plate, list):
            # Går gjennom hvert element i 'plate' og ser om den har element som er lengre en de lengste elementene
            # I listen med plater
            for index, element in enumerate(plate):
                if len(element) > length_formatting[index]:
                    # Endrer elementet i 'length_formatting' i indeksen 'index' til lengden av 'element'
                    length_formatting[index] = len(element)

                    # Lagrer endringen til filen './libraries/data/max_lengths.json'
                    update_data(FILEPATH_LENGTHS, length_formatting)

            # Henter alle ID'ene til plate objektene og legger dem sammen i en liste
            id_list = [plate["ID"] for plate in plates]

            # Kjøres helt til det blir laget en ID som ikke allerede er brukt
            while True:

                # Lager en ID med 4 tilfeldige tall og bokstaver
                ID = "".join(choices(ascii_lowercase + digits, k=4))

                # Sjekker om 'ID' er i 'id_list'
                if ID not in id_list:
                    break

            # Tar 'plate' og unpacker listen og legger inn i klassen 'PlateObject' og
            # får tilbake en ordbok som legges til i 'plates'
            plates.append(PlateObject(ID, *plate).__dict__)

            # Lagrer endringene til filen './libraries/data/platelist.json'
            update_data(FILEPATH_PLATES, plates)
            print("\nPlate ble lagt til i 'platelist.json'!")

        # Om 'plate' ikke er en liste, kjører koden under
        else:
            print(f"\n{Colors.error}An error has occured, the plate was not saved{Colors.endc}")

    # Skriver en velkommstmelding når programmet starter
    welcome_message()

    # Starter en loop som går til programmet avsluttes.
    while True:
        try:

            # Tar brukerinput og definerer det til 'user_input'
            user_input = input(f"\n{Colors.bold}Main > {Colors.endc}").split(" ")

            # Sjekker om første ordet brukeren skrev er i listen med kommandoer
            if (command := user_input[0]) in commands:

                # Definerer 'func' som funksjonen i listen 'commands' med nøkkelen 'command' på indeks 0 i tuplen
                func = commands[command][0]

                # Ser om 'command' er "help"
                if command == "help":

                    # Kjør funksjonen til "help"
                    func(commands)

                # Ser om 'command' er "find"
                elif command == "find":

                    # Defienrer 'search_list' som resulatet til funksjonen til 'commands['find'][0]'
                    search_list = func(plates, user_input[1], user_input[2:])

                    # Sjekker om 'search_list' er i string form
                    if isinstance(search_list, str):
                        print(f"{Colors.error}'{user_input[1]}' er ikke gydlig.. bruk 'hjelp' for mer informasjon om 'find'{Colors.endc}")

                    # Sjekker at listen 'search_list' ikke har 0 elementer
                    elif len(search_list) != 0:

                        # Skriv ut en fin liste av elementene med 'print_list()'
                        print_list(search_list, length_formatting)

                    # Hvis det er 0 elementer i listen, skriv ut:
                    else:
                        print("Fant ingen plater..")

                # Sjekker om command er "list"
                elif command == "list":

                    # Kjører kommandoen til "list" med parameterene 'plates' og 'length_formatting'
                    func(plates, length_formatting)

                # Sjekker om command er "remove"
                elif command == "remove":

                    # Ser om antall elementer 'user_input' ikke er 2
                    if len(user_input) != 2:

                        # Hvis sant, skriv ut error, og kall exception 'Restart'
                        print("brukes: remove [ID]. les mer med 'help'")
                        raise Restart

                    # Finner indeksen til platen som brukeren ønsker å fjerne
                    index: int = [plates.index(plate) for plate in plates if plate['ID'] == user_input[1].lower()][0]

                    # Ser om funksjonen til "remove" med parameteren 'plates[index]' returnerer sant
                    if func(plates[index]):

                        # Hvis sant, fjern objektet i 'plates' med indeksen 'index'
                        plates.pop(index)

                        # Skriv endringene i listen 'plates' til 'FILEPATH_PLATES'
                        update_data(FILEPATH_PLATES, plates)

                # Sjekker om command enten er "newplate" eller "quickadd"
                elif command == "addplate" or command == "quickadd":

                    # kjører funksjonen til "newplate" eller "quickadd" og
                    # Lagrer endringene til filen './libraries/data/platelist.json'
                    save_plate(func())

                # Sjekker om command er "random"
                elif command == "random":

                    # Skriver ut en fin liste av listen returnert av funksjonen til "random"
                    print_list(func(plates), length_formatting)

                # Hvis 'command' ikke stemmer med noen over, prøv å kjøre funksjonen til 'command' i 'commands'
                else:
                    func()

            # Kjøres hvis 'command' ikke er et element i 'commands'
            else:
                print(f"{Colors.error}'{command}' er ikke en gyldig command... "
                      f"Bruk 'help' for å se gyldige kommandoer{Colors.endc}")

        except IndexError:
            print(f"{Colors.error}fant ikke platen, eller så er det du har oppgitt ugyldig.. bruk 'help' for mer info {Colors.endc}")

        except Restart:
            pass

        except KeyboardInterrupt:
            exit()


main()
