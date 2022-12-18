# Innlevering 7 - Oppgave:

En god venn av deg har en veldig stor platesamling. Hen ønsker å organisere samlingen sin 
ved hjelp av et program, og det er sikkert flere andre som ønsker seg et slikt program.

En platesamling har en eier og består av mange album. Albumene er enten på CD eller på 
vinyl (LP). Felles for de to er at et album alltid har en artist, et plateselskap og et utgivelsesår. 
Vinyl skiller seg fra en CD ved at den kan spilles av med to ulike hastigheter, enten 33 rpm 
(rotasjoner per minutt) eller 45 rpm. Vinyler kan også lages med ulik farge.
Lag et program som skal inneholde en datastruktur som samler dataene om samlingen.
Lag et eget bibliotek som man kan bruke til å:

- registrere nye CD-er og venyler
- vise en oversikt over en bestemt plate i samlingen
- vise en oversikt over alle plater i samlingen
- vise en oversikt over alle artister i samlingen
- vise en oversikt over alle platene til en gitt artist
- velge for deg en tilfeldig plate til avspilling. Som resultat vil det bli skrevet album og år.

Lag flere funksjoner i biblioteket som kan være kjekt å ha i forbindelse med bruk av 
samlingen.

Husk å dokumentere tydelig både hvordan biblioteket kan brukes, men også i koden.

## Informasjon om gjennomføring av oppgaven

I denne oppgaven ønsket jeg virkelig få frem og vise mine kunnskaper i faget, samt å utfordre meg selv. Jeg valgte å gjøre oppgaven på en måte hvor jeg har brukt fagstoff som vi ikke har vært gjennom enda. Jeg valgte å lage programmet i terminalstil, der brukeren kan skrive inn ulike kommandoer og få resultater. Dette gir brukeren en følelse av frihet mens programmet brukes.

Jeg valgte også å ta inn og bruke json-filer. Dette fordi som oppgaven sier, ønsker en god venn av meg å organisere en stor samling han har ved hjelp av et program, samt muligens andre personer også. Dermed gir det mening å implementere evnen for programmet å hente og skrive informasjon slik at alt lagres etter bruk. Hvis ikke, hadde programmet aldri lagret de ulike platene etter bruk. 

Denne filen laget fordi jeg hadde ekstra tid, og ønsket å lære å skrive gode ***README.md*** files også. Nedenfor på "Bruk av Funksjonene" la jeg inn funksjonene selv om det ville vært lettere å lese koden. Men som sagt så gjorde jeg dette bare for gøy.


## Biblotek informasjon

Obs! Biblotekene ble i hovedsak laget for å fungere i dette programmet, og det kan dermed hende at ulike funksjoner ikke passer bra sammen med andre programmer.

Prosjektet bruker ingen ingen tredjeparts biblotek, som betyr at du ikke trenger noe annet en python3 for å kjøre programmet. Men den bruker innebygde biblotek som ***'random'*** og ***'json'***.

I prosjekt mappen finner du en mappe som heter 'libraries'. Denne listen inneholder alle biblotekene som brukes i programmet. Det er fire python filer:

- ***platelibrary.py***, som inneholder de fleste funksjonene som handler om platene. Som modifisering av spesifikke plater, legge til nye, fjerne en plate, osv.

- ***interface.py***, brukes til å skrive ut velkommstmelding og en strukturert liste.

- ***filehandling.py***, inneholder kode som brukes til å lagre data til '.json' filer. Den har to funksjoner: ```get_data(data)``` og ```update_data(Filepath, data)```.

- ***classes.py***, inneholder to klasser: ```PlateObject``` og ```Colors```

Funksjonene fra disse biblotekene skal fungere utenom hovedprogrammet ***main.py***. Koden i de forskjellige biblotekene skal være godt dokumenter. 

## Bruk av Funksjonene

*Du finner den faktiske koden i filene*


Funksjonene i ***platelibrary.py***

```python
def random_plate(plates: list[dict]):
    """ Funksjonen henter en tilfeldig plate fra 'platelist.json' og returnerer den

    :param plates: liste med plater
    :return: en plate
    """


def find_plates(plates, search_type, search_words):
    """ Funksjon som leter etter spesifikke plater etter hva brukeren ser etter

    :param plates: Listen med plater
    :param search_type: Hvilken kategori brukeren søker i
    :param search_words: Hva brukeren søker etter
    :return: en liste med platene som ble funnet
    """


def remove_plate(plate):
    """ Funksjon som spør om brukeren ønsker å slette platen som er valgt

    :param plate: Platen som brukeren ønsker å fjerne
    :return: 'True' eller 'False' om brukeren ønsker å fjerne eller ikke
    """


def plate_quickadd():
    """ Brukes som en raskere måte å lage en ny plate
    
    :return: En liste med alle elementene som platen trenger
    """

    def lastpart():
        """ Nested funksjon som bare brukes i denne funksjonen. Brukes når listen nesten er ferdig

        :return 'plate' eller 'False' om brukeren avslutter
        """


def plate_add():
    """ Brukervennelig funksjon som lager et nytt plate element i liste form

    :return: En liste med 7 elementer
    """
```


Funksjonene i ***Interface.py***:

```python
def welcome_message():
    """ Skriver ut en velkommst melding
    """


def print_commands(commands):
    """ Funksjon som viser en liste over alle kommandoer som kan brukes og informasjon om dem

    :param commands: Parameteren tar inn en ordbok med kommandoer
    """


def print_list(plates, lengths):
    """ Funksjonen skriver ut alle platene 'plates' til konsollen i tabell form

    :param plates: Liste med plater
    :param lengths: Liste med 7 int elementer
    """
```

Funksjonene i ***filehandling.py***:

```python
def get_data(filepath: str):
    """ Henter data fra filbanen 'filepath'

    :param filepath:
    :return: dataen fra filen som har filbanen 'filepath'
    """


def update_data(filepath: str, new_data):
    """ Bytter ut dataen i 'filepath' med 'new_data'
    
    :param filepath: String med filbanen til filen 
    :param new_data: Dataen som skal bli bytta inn i filen
    """

```

Funksjonene i ***classes.py***:

```python
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


class Colors:
    """ En klasse for å definere farger for tekst utskrift i terminalen.
    """
```

## Json-filer

Det er to json-filer som har blitt brukt i programmet, dette er ***max_lengts.json*** og ***platelist.json***

- ***platelist.json***, inneholder en liste med dictionaries som hver har 8 elementer i seg: ID, Artist, Album, Plateselskap, År, Format, Avspillingshastighet og Farge. 

- ***max_lengts.json***, inneholder 8 heltall i en liste. Hvert heltall representerer det lengste elementet og ligger parallelt med tilsvarende element i den andre json-filen ***platelist.json***


##

Et prosjekt av: ***Adrian Egelandsdal Skeie***