"""
Filen inneholder alt som omhandler plater, som laging, fjerning og modifisering.

OBS: Klassene som brukes i denne filen er bare brukt til feilmeldinger i denne filen og er derfor plassert her
og ikke i 'classes.py'
"""

from os import system, name
from .classes import Colors
from random import choice

# Liste med ulike elementer som brukes til å sjekke om brukeren ønsker å stoppe
stop_commands = ["stop", "avslutt", "exit", "avbryt", "quit", "tilbake", "restart"]

"""
Klassene under brukes til egendefinerte feilmeldinger
"""


class Restart(Exception):
    pass


class FormatError(Exception):
    pass


class HastighetUgyldig(Exception):
    pass


class ValError(Exception):
    pass


# ------------ #


def clear():
    """ Renser konsollen for all tekst

    """

    # Utfører kommandoene 'cls' eller 'clear' avhengig av operativsystemet
    system("cls" if name == "nt" else "clear")


def stop():
    """ Brukes til å avslutte programmet

    :return: Returnerer 'True' eller 'False' ettersom brukeren ønsker å avslutte eller ikke
    """

    while True:

        # Definerer 'choice' som bruker input
        choice = input("Er du sikker på at du vil avslutte? ingenting vil bli lagret!\nJa/Nei: ").lower()

        # Sjekker om 'choice' er "nei"
        if choice == "nei":

            # Hvis sant, tilbakestill platetype
            plate_type = ""

            return False

        # Hvis ikke, sjekk om svar er 'ja'
        elif choice == "ja":
            return True

        # Visst ikke, skriv feilmelding
        else:
            print(f"{Colors.error}du må skrive 'Ja' eller 'Nei'..{Colors.endc}")


def random_plate(plates: list[dict]):
    """ Funksjonen henter en tilfeldig plate fra 'platelist.json' og returnerer den

    :param plates: liste med plater
    :return: en plate
    """
    return [choice(plates)]


def find_plates(plates, search_type, search_words):
    """ Funksjon som leter etter spesifikke plater etter hva brukeren ser etter

    :param plates: Listen med plater
    :param search_type: Hvilken kategori brukeren søker i
    :param search_words: Hva brukeren søker etter
    :return: en liste med platene som ble funnet
    """
    try:

        # Ordbok med mulige søk
        types = {"-ar": "Artist", "-al": "Album", "-ps": "Plateselskap", "-id": "ID"}

        # Finner typen søk brukeren ønsker
        search_type = types[search_type]

        # Legger sammen ordene brukeren søker etter og gjør teksten til små bokstaver
        search_words = " ".join(search_words).lower()

        # Definerer en midlertidig liste som brukes til å lagre alle platene som funksjonen finner
        temp = []

        # Går gjennom hver plate i 'plates'
        for index, plate in enumerate(plates):

            # Definerer 'string' som inneholder teksten fra typen brukeren leter etter og gjør den til små bokstaver
            string = plate[search_type].lower()

            # Sjekker om 'string' er lengre eller lik det brukeren søker etter
            if len(string) >= len(search_words):

                # Sjekker om hva brukeren søker etter matcher 'string' forkortet til like mange bokstaver som søke ordet
                if search_words == string[:len(search_words)]:
                    # Visst det stemmer, legges platen til i listen'temp'
                    temp.append(plates[index])

                # Hvis ikke, sjekkes det om 'search_words' bare er ett ord
                elif len(search_words.split()) == 1:

                    # Går gjennom hvert ord i 'string'
                    for word in string.split():

                        # Sjekker om ordet er likt eller delvis likt
                        if word[:len(search_words)] == search_words:

                            # Hvis sant legg til i listen 'temp' og bryt ut av for-løkka
                            temp.append(plates[index])
                            break

        # Til slutt returneres listen
        return temp

    except KeyError:
        return f"'{search_type}' er ugyldig"


def remove_plate(plate):
    """ Funksjon som spør om brukeren ønsker å slette platen som er valgt

    :param plate: Platen som brukeren ønsker å fjerne
    :return: 'True' eller 'False' om brukeren ønsker å fjerne eller ikke
    """
    while True:
        print(" | ".join(str(element) for element in plate.values()))
        answer = input(f"\n{Colors.warning}Er du sikker på at du vil fjerne platen? Ja/Nei\n >  {Colors.endc}").lower()

        return True if answer == "ja" else False


def plate_quickadd():
    """ Brukes som en raskere måte å lage en ny plate

    :return: En liste med alle elementene som platen trenger
    """

    def lastpart():
        """ Nested funksjon som bare brukes i denne funksjonen. Brukes når listen nesten er ferdig

        :return 'plate' eller 'False' om brukeren avslutter
        """

        while True:

            # definerer 'answer' som input fra brukeren
            answer = input(f"\nListen ser sånn ut: {plate}\n"
                           "'save' om du ønsker å lagre. Eller tallet til elementene for å endre.\n"
                           "Første elementet er 1, og siste 7.\n\n> ")

            # Hvis svaret er et element i en liste med tall i tekst form fra 1 til 7:
            if answer in list(map(str, range(1, 8))):

                # Spør brukeren om å skrive inn endring i indeksen som er valgt
                plate[int(answer) - 1] = input(f"Endre '{plate[int(answer) - 1]}' til > ")

            # Sjekker om brukeren ønsker å lagre, returnerer 'plate' om sant
            elif answer.lower() == "save":
                return plate

            # Sjekker om brukeren ønsker å avslutte, returnerer False om brukeren ønsker
            elif answer.lower() in ["avslutt", "exit", "avbryt"]:
                return False

    # Definerer 'liste' som en liste med ulike string element
    liste = ["Artist", "Album", "Plateselskap", "År", "Format", "Avspillingshastighet", "Farge"]

    while True:
        print(f"\n{Colors.red_text}Skriv inn som dette: {','.join(liste)}{Colors.endc}\n\nquickadd > ", end="")

        """
        Definerer en variabel plate. Den skal inneholde en liste av elementer som blir oppdelt fra en string
        hvor det er komma.
        """
        # definerer en midlertidig liste
        temporary_list = input().split(",")

        # Definerer variabelen som skal holde dataen til platen
        plate = []

        # Fjerner mellomrom istarten av elementene om det skulle være det.
        for element in temporary_list:
            plate.append(element.lstrip())

        # Sjekker om listen 'plate' har mer en 7 elementer
        if len(plate) > 7:

            print(f"\n{Colors.warning}Du har for mange elementer i listen... Fjerner alle som overstiger{Colors.endc}")

            # Listen 'plate' blir definert til seg selv, men bare med de første 7 elementene
            plate = plate[:7]

        # Sjekker om listen 'plate' har mindre en 7 elementer
        elif len(plate) < 7:
            print(f"Du må legge til {7 - len(plate)} plate(r) til")
            # Ber om nødvendige element slik at listen har 7 elemmenter
            for nummer in range(7 - len(plate)):
                plate.append(input(f"{nummer + 1}. ").lstrip())

        # Hopper til de siste stegene til funksjonen
        return lastpart()


def plate_add():
    """ Brukervennelig funksjon som lager et nytt plate element i liste form

    :return: En liste med 7 elementer
    """

    # Definerer noen variabler som bruekes senere i programmet
    plate_type = ""
    hastighet = "-"
    farge = "-"
    year = ""

    print("Du lager nå en ny plate.\n")

    # Koden under kjører til den blir avbrutt av brukeren
    while True:
        try:
            # Sjekker om 'plate_type' er "CD" eller "LP", hvis ikke:
            if plate_type not in ["CD", "LP"]:

                # Spør etter plate type
                plate_type = input("Hvilken type er platen? Vinyl (LP) eller CD: ").upper()

                # Sjekker om 'plate_type' er i 'stop_commands
                if plate_type.lower() in stop_commands:
                    # Hvis sant, kall funksjonen 'stop()'
                    if stop():
                        break
                    # Hvis 'stop()' ikke er sann, kall på exception 'Restart'
                    else:
                        raise Restart

                # Sjekker om 'plate_type' er "Vinyl'
                if plate_type == "VINYL":

                    # Gjør 'plate_type' til "LP"
                    plate_type = "LP"

                # Hvis 'plate_type' ikke er "CD" eller "LP", kall på exception 'FormatError'
                if plate_type not in ["CD", "LP"]:
                    raise FormatError

            # Sjekker om 'plate_type' er "LP" og 'hastighet' ikke er i listen under
            if plate_type == "LP" and hastighet not in ["33 rpm", "45 rpm"]:

                # Definerer 'hastighet' som bruker input
                hastighet = input("Avspillingshastighet: ").lower()

                # Sjekker om 'hastighet' er et element i 'stop'commands'
                if hastighet in stop_commands:
                    if stop():
                        break

                    # Hvis 'stop()' ikke er sann, kall på exception 'Restart'
                    else:
                        raise Restart

                # Sjekker om hastighet er "33"
                if hastighet == "33":

                    # Gjør 'hastighet' til:
                    hastighet = "33 rpm"

                # Sjekker om hastighet er "45"
                if hastighet == "45":

                    # Gjør 'hastighet' til:
                    hastighet = "45 rpm"

                # Hvis 'hastighet' ikke er et element i listen under, kall på expeption 'HastighetUgyldig'
                if hastighet not in ["33 rpm", "45 rpm"]:
                    raise HastighetUgyldig

            # Sjekker om 'plate_type' er "LP" og 'farge' ikke har blitt gitt en farge
            if plate_type == "LP" and farge == "-":

                # Redefinerer 'farge' som bruker input
                farge = str(input("Oppgi fargen til platen: "))

                # Ser om 'farge' er et element i stop_commands
                if farge.lower() in stop_commands:
                    # Hvis sant, kall funksjonen 'stop()'
                    if stop():
                        break

                    #  Hvis 'stop()' ikke er sann, kall på exception 'Restart'
                    else:
                        raise Restart

                # Spør om bekreftelse på at fargen som er oppgitt er riktig
                if input(f"{Colors.warning}Du har oppgitt '{farge}'. Ønsker du å fortsette? Y/N {Colors.endc}").upper() == "N":

                    # Hvis ikke, sett 'farge' lik "-"
                    farge = "-"

                    # gå tilbake tilbake og prøv igjen
                    raise Restart

            # Sjekker om året til platen ikke er oppgitt
            if year == "":

                # Definerer 'year' som heltall av brukerinput
                year = int(input("\nÅret utgitt: "))

                # Sjekker om plate typen er "CD" og at 'year' ikke er mindre en 1982 (første CD plate lansert 1982)
                if plate_type == "CD" and year < 1982:

                    # Endrer 'year' tilbake til en tom string
                    year = ""

                    print(f"\n{Colors.error}Utgivelse datoen til en CD plate kan ikke være før 1982{Colors.endc}")

                    # Går tilbake til toppen av while-løkka
                    raise Restart

                # Sjekker om plate typen er "LP" og at 'year' ikke er mindre en 1948 (første vinyl plate lansert 1948)
                elif plate_type == "LP" and year < 1948:

                    # Endrer 'year' tilbake til en tom string
                    year = ""

                    print(f"\n{Colors.error}Utgivelse datoen til en Vinyl plate kan ikke være før 1948{Colors.endc}")

                    # Går tilbake til toppen av while-løkka
                    raise Restart

                else:

                    # Avslutter med å gjøre 'year' til en string
                    year = str(year)

            # Spør om resten av informasjonen, samt legger variablene over inn i en liste 'plate'
            plate = [input("Artistens navn: "), input("Albumet: "), input("Plateselskapeet: "),
                     year, plate_type, hastighet, farge]

            # Går til slutt delen hvor brukeren kan endre på den oppgitte informasjonen, eller lagre platen
            while True:

                # Renser konsollen fra all tekst
                clear()
                try:
                    print("\nListen under er skrevet i denne rekkefølgen -> Artist | Album | Plateselskap | "
                          "År | Format | Avspillingshastighet | Farge\n")

                    print(Colors.warning)
                    print(" | ".join(plate))
                    print(Colors.endc)

                    print("Sånn ser platen ut. Ønsker du å gjøre noen endringer? "
                          "Skriv nummeret hvor det du vil endre er plassert\n"
                          "eller 'save' om det ser fint ut. eller 'cancel' for å avbryte")

                    # Ber brukeren skrive inn hva som ønskes å gjøre
                    user_input = input("> ").lower()

                    if user_input == "cancel":
                        return False

                    # Sjekk om 'user_input' ikke er "save"
                    if user_input == "save":
                        return plate

                    # Sjekker om 'user_input' er et element i en liste med tall i string form fra og med 1 til og med 7s
                    if user_input in list(map(str, range(1, 8))):
                        # Omgjør 'user_input' til heltall og tar ifra 1
                        user_input = int(user_input) - 1

                    else:
                        raise ValError

                    # Sjekker om 'user_input' er et heltall fra og med 0 til og med 7
                    if 0 <= user_input <= 7:

                        print("Om du ikke ønsker å endre noe, ikke skriv inn noe")

                        # Ber brukeren om å skrive inn endringen
                        change = input(f"Du endrer '{plate[user_input]}' til > ")

                        # Sjekker om 'change' ikke er en tom tekst
                        if change != "":

                            # Endre indeksen 'user_input' i listen 'plate' til 'change'
                            plate[user_input] = change
                    else:
                        raise ValError

                except ValError:
                    print(f"\n{Colors.error}Du har oppgitt et tall som ikke korresponderer "
                          f"til et element i listen.. Det første objektet er 1{Colors.endc}")

        except Restart:
            pass

        except FormatError:
            print("Formaten du har oppgitt er ikke gyldig.. Den må være LP eller CD")

        except HastighetUgyldig:
            print("Hastigheten du har oppgitt er ikke gyldig.. Den må være 33 eller 45")

        except ValueError:
            year = ""
            print(f"\n{Colors.error}Årstallet må være oppgitt som et nummer...{Colors.endc}")

        except KeyboardInterrupt:
            exit()