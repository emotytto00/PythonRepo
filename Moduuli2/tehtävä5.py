leiviskä = float(input('Anna leiviskät'))
naula = float(input('Anna naulat'))
luoti = float(input('Anna luodit'))

luotiM = 13.3
naulaM = (luotiM)*32
leiviskäM = (luotiM)*20*32
massa = ((luoti + luotiM) * (naulaM + naula) * (leiviskäM + leiviskä))

kilot = int(massa/1000)
grammat = (massa/1000 - (int(massa/1000)))*1000
print(f'Massa nykymitoissa: {kilot} kg {grammat} g')


