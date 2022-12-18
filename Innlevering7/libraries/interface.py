"""
Denne filen blir brukt til det meste visuelle i hovedprogrammet
"""
from .classes import Colors


def welcome_message():
    """ Skriver ut en velkommst melding
    """

    print("Velkommen til platesamling organisereren!\nBruk 'help' for å se kommandoer")


def print_commands(commands):
    """ Funksjon som viser en liste over alle kommandoer som kan brukes og informasjon om dem

    :param commands: Parameteren tar inn en ordbok med kommandoer
    """

    for command in commands:
        print("{:>{}} {:{}} {}".format("-", 4, command, 10, commands[command][1]))


def print_list(plates, lengths):
    """ Funksjonen skriver ut alle platene 'plates' til konsollen i tabell form

    :param plates: Liste med plater
    :param lengths: Liste med 7 int elementer
    """

    # Definerer en midlertidig liste med topdelen av tabellen
    temporary_list = ["ID", "Artist", "Album", "Plateselskap", "År", "Format", "Avspillingshastighet", "Farge"]

    # Lager en ny linje før hele tabellen blir skrevet ut
    print()

    # Går gjennom 'temporary_list' og skriver det ut på en strukturert måte
    for index, element in enumerate(temporary_list):
        # Printer 'element' fra 'temporary_list' på en fin måte
        print(f"{element:<{lengths[index]}}", end=" | ")

    # Lager et mellomrom
    print()

    # brukes til å lage en linje med '-' like lang som total lengden til det over
    for length in lengths:
        print("-" * length, end="-+-")
    print()

    # Går gjennom listen 'plates' og skriver det ut på en strukturert måte
    for index_plate, objekt in enumerate(plates):

        # Endrer fargen til rød eller blank avhengig om indeksen er partall eller ikke. Dette er for å skille elementer
        # I tabellen lettere.
        print(Colors.red_text if (index_plate % 2) == 0 else Colors.endc, end="")

        # Går gjennom hvert element i objektet, og skriver det ut på en strukturert måte
        for index_element, element in enumerate(objekt.values()):
            print(f"{element:<{lengths[index_element]}}", end=" | ")

        # Tilbakestiller fargen i terminalen (Om det er noen endringer)
        print(f"{Colors.endc}")

    # Tilbakestiller fargene i terminalen (Om det er noen endringer)
    print(Colors.endc)