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