lentoasemat = {
    'EFHK' : 'Helsinki-Vantaan Lentoasema', '42OK' : 'Kingston international airport',
}
hakusana = [lentoasemat]
teko = str
while teko != '':
    teko = input('Syötä uusi, hae entistä tai lopeta: ')
    if teko in lentoasemat:
        print(lentoasemat[hakusana])
    else:

lentoasemat['AGRG'] = 'Ulawa Airport'
lentoasemat['SJRM'] = 'Seinäjoen tango airport'

