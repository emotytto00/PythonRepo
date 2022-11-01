import random
from tabulate import  tabulate

class Auto:
    def __init__(self, rekkari, huippunopeus, nopeus, matka):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdytä(self, muutos):
        self.nopeus = min(self.nopeus + muutos, self.huippunopeus)
        self.nopeus = max(self.nopeus, 0)
        return

    def kulje(self, tunnit):
        self.matka = self.matka+(self.nopeus*tunnit)


class Kilpailu:
    def __init__(self, nimi, km, auton_teko):
        self.nimi = nimi
        self.km = km
        self.tunti = 0
        self.autot = []
        self.auton_teko = auton_teko
        for i in range(auton_teko):
            auton_teko = Auto("ABC-"+str(i), random.randint(100, 200), 0, 0)
            self.autot.append(auton_teko)

    def kilpailu_ohi(self):
        self.ohi = False
        for Auto in self.autot:
            if Auto.matka > self.km:
                self.ohi = True
                return self.ohi

    def tunti_kuluu(self):
        self.tunti += 1
        for Kilpailu.auton_teko in self.autot:
            Kilpailu.auton_teko.kiihdytä(random.randint(-10, 15))
            Kilpailu.auton_teko.kulje(1)

    def tulosta_tilanne(self):
        loppu = []
        for self.auton_teko in self.autot:
            loppu.append((self.auton_teko.rekkari, self.auton_teko.huippunopeus, self.auton_teko.nopeus, self.auton_teko.matka, self.tunti))
        if self.tunti % 10 == 0 or self.kilpailu_ohi():
            print(tabulate(loppu, headers=['Rekisteri', 'Huippunopeus', 'Nopeus', 'Matka', 'Kuluneet tunnit'], tablefmt='Double Grid'))

kilpailu1 = Kilpailu('Piston cup', 8000, 10)

while not kilpailu1.kilpailu_ohi():
    kilpailu1.tunti_kuluu()
    kilpailu1.tulosta_tilanne()
