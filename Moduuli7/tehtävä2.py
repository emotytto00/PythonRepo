nimet = set()
nimi = str

while nimi != '':
    nimi = input('Syötä nimi tai tyhjä merkkijono: ')
    if nimi in nimet:
        print('Tää nimi on jo syötetty bro')
    else:
        print('Wau leija nimi G!! Laitetaanpi listaa.')
        nimet.add(nimi)
for t in nimet:
    print(t)