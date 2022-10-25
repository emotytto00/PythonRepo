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

auto = Auto("ABC-123", 142)
auto.kiihdytä(30)
print(f'{auto.nopeus}')
auto.kiihdytä(70)
print(f'{auto.nopeus}')
auto.kiihdytä(50)
print(f'{auto.nopeus}')
auto.kiihdytä(-200)
print(f'{auto.nopeus}')

auto.kiihdytä(70)
auto.kulje(3)
print(f'Nopeus {auto.nopeus} km/h, {auto.matka} km kuljettu')