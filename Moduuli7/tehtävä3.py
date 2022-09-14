lentoasemat = {
    'EFHK' : 'Helsinki-Vantaan Lentoasema', 'HHOK' : 'Kingston international airport',
}
hakusana = [lentoasemat]
teko = str
while teko != '':
    teko = input('Syötä uusi (uusi) '
                 'Hae entistä (hae) '
                 'Lopeta syöttämällä tyhjä: ')
    if teko.upper() == "UUSI":
        nimi = input('Anna lentoaseman nimi: ')
        lentoasemat[input('Anna aseman ICAO koodi: ')] = nimi

    if teko.upper() == "HAE":
        ICAO = input('Syötä aseman ICAO koodi: ')
        print(f'koodilla {ICAO} löytyi lentokenttä: {lentoasemat[ICAO]}')
else:
    print('Ohjelma lopetetaan. Prepare for selfdestruction in 5,4,3,2,1... BOOOOMM!!!!!')




lentoasemat['AGRG'] = 'Ulawa Airport'
lentoasemat['SJRM'] = 'Seinäjoen tango airport'

