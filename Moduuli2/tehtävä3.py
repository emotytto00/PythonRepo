kanta_str, korkeus_str = input("Syötä suorakulmaisen kolmion kanta ja korkeus").split()
kanta = float(kanta_str)
korkeus = float(korkeus_str)
print(f'kolmion pinta-ala on: {(kanta * korkeus)/2}')