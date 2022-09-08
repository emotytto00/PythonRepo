numerot = []

numero = input('Anna ensimmäinen luku tai syötä tyhjä')
while numero != "":
    numerot.append(numero)
    numero = input('Anna toinen luku tai syötä tyhjä')
    numerot.sort(reverse=True)
print(numerot[0:5])
