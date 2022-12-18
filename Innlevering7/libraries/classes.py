# Filen inneholder klassene som brukes i programmet


# Klassen som blir brukt til å lage nye plateelement til listen med plater.
class PlateObject:
    """
    En klasse som representerer en plate
    """
    def __init__(self, ID, artist, album, plateselskap, year, format, avspillingshastighet, farge):
        """ Initialiserer Plate-objektet

        Argumenter:
            :param artist: Navnet til en Artist
            :param album: Navnet på albummet
            :param plateselskap: Navnet på plateselskapet
            :param year: Utgivelsesåret
            :param format: Formaten platen står i
            :param avspillingshastighet: Avspillingshastigheten til platen om relevant s(Bare på Vinyl (LP) plater)
            :param farge: Fargen til platen om relevant (Bare på Vinyl (LP) plater)
        """
        self.ID = ID                                      # IDen til objektet
        self.Artist = artist                              # Navnet på artisten
        self.Album = album                                # Navnet på albumet
        self.Plateselskap = plateselskap                  # Plateselskapet som utga platen
        self.year = year                                  # Året platen ble utgitt
        self.Format = format                              # Formaten på platen (f.eks. vinyl eller cd)
        self.Avspillingshastighet = avspillingshastighet  # Avspillingshastighetetn til platen (f.eks
        self.Farge = farge                                # Fargen på platen (Om relevant)
        return


class Colors:
    """ En klasse for å definere farger for tekst utskrift i terminalen.
    """
    green = '\033[92m'
    warning = '\033[93m'
    error = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    red_text = "\033[1;37;31m"