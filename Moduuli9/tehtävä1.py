class Auto:
    def __init__(self, rekkari, huippunopeus, nopeus, matka):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka


auto = Auto("UKG-542", "142 km/h", 0, 0)
print (f"{auto.rekkari:s} on rekkari ja huippunopeus {auto.huippunopeus:s}" )