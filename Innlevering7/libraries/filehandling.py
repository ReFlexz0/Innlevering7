import json


def get_data(filepath: str):
    """ Henter data fra filbanen 'filepath'

    :param filepath:
    :return: dataen fra filen som har filbanen 'filepath'
    """

    # Åpner filen for lesing
    with open(filepath) as filedata:
        # Laster inn og returnerer data fra filen som er lastet inn.
        return json.load(filedata)


# Oppdaterer data i en json-fil
def update_data(filepath: str, new_data):
    """ Bytter ut dataen i 'filepath' med 'new_data'

    :param filepath: String med filbanen til filen
    :param new_data: Dataen som skal bli bytta inn i filen
    """
    # Åpner filen for skriving
    with open(filepath, "w") as filedata:
        # Erstatter dataen i json-filen med "plateliste"
        json.dump(new_data, filedata, indent=4)