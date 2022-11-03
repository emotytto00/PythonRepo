import random
from tabulate import  tabulate

class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus = min(self.nopeus + muutos, self.huippunopeus)
        self.nopeus = max(self.nopeus, 0)
        return

    def kulje(self, tunnit):
        self.matka = self.matka+(self.nopeus*tunnit)

    def tulosta(self):
        print(f'Rekisterinro: {self.rekkari}, Mittarilukema: {self.matka}')

class Sähköauto(Auto):
    def __init__(self, rekkari, huippunopeus, akku):
        self.akku = akku
        super().__init__(rekkari, huippunopeus)

    def tulosta(self):
        super().tulosta()
        print(f'Akkukapasiteetti: {self.akku} kw/h')

class Polttomoottori(Auto):
    def __init__(self, rekkari, huippunopeus, tankki):
        self.tankki = tankki
        super().__init__(rekkari, huippunopeus)

    def tulosta(self):
        super().tulosta()
        print(f'Bensatankin tilavuus: {self.tankki} L')



lista = []
i = 1
a = 0
s = 0

while i != 11:
    lista.append(Auto("ABC-"+str(i), random.randint(100, 200)))
    i += 1

while lista[a].matka != 10000:
    lista[a].kiihdytä(random.randint(-10, 15))
    lista[a].kulje(1)
    a += 1
    if a == 10:
        a = 0
    if lista[a].matka > 10000:
        break

while s != 10:
    table = [[f'Auto {s+1} rekisterillä {lista[s].rekkari}'], [f'Huippunopeus {lista[s].huippunopeus}'], [f'tämän hetkinen nopeus {lista[s].nopeus}'], [f'matka ajettu {lista[s].matka}']]
    print(tabulate(table))
    s += 1

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

Auto("ABC-15", 180)
Auto("ACD-123", 165)
s = Sähköauto("ABC-15", 180, 52.5)
p = Polttomoottori("ACD-123", 165, 32.3)

s.kiihdytä(50)
p.kiihdytä(100)

s.kulje(3)
p.kulje(3)

s.tulosta()
p.tulosta()