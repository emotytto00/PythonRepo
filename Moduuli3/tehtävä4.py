vuosi = int(input('Anna vuosiluku: '))

tulos = 'ei ole'

if vuosi % 4 == 0:
    if vuosi % 100 != 0:
        tulos = 'on'
    if vuosi % 400 == 0:
        tulos = 'on'

print(f'vuosi {vuosi} {tulos} karkausvuosi')
