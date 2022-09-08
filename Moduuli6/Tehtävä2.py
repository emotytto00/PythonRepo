import random

def noppa(tahkot):
    return random.randint(1, tahkot)

tahkot = int(input('Anna suurin silmäluku: '))

luku = 0
while luku != tahkot:
    luku = noppa(tahkot)
    print(luku)
    if luku == tahkot:
        print('Maksimi saavutettu!')
