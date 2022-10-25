class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0


auto = Auto("ABC-123", "142 km/h")
print(f"{auto.rekkari}, {auto.huippunopeus:}, {auto.nopeus}, {auto.matka}")