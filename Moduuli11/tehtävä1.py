class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f'Julkaisun nimi: {self.nimi}')

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivulkm):
        self.kirjailija = kirjailija
        self.sivulkm = sivulkm
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Kirjailija: {self.kirjailija} | Sivumäärä: {self.sivulkm}')

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Päätoimittaja: {self.päätoimittaja}')

#pääohjelma
Julkaisu('Aku Ankka')
Julkaisu('Hytti n:o 6')
k = Kirja('Hytti n:0 6', 'Rosa Liksom', '200')
l = Lehti('Aku Ankka', 'Aki Hyyppä')
k.tulosta_tiedot()
l.tulosta_tiedot()