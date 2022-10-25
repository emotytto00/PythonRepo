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

auto = Auto("ABC-123", 142)
auto.kiihdytä(30)
print(f'{auto.nopeus}')
auto.kiihdytä(70)
print(f'{auto.nopeus}')
auto.kiihdytä(50)
print(f'{auto.nopeus}')
auto.kiihdytä(-200)
print(f'{auto.nopeus}')

print(f'{auto.rekkari}, {auto.huippunopeus} km/h, {auto.matka}')