leiviskä = float(input('Anna leiviskät'))
naula = float(input('Anna naulat'))
luoti = float(input('Anna luodit'))

luotiM = float(13.3 * luoti)
naulaM = float(32 * luoti)
leiviskäM = float(20 * naula)
massa = (luotiM + naulaM + leiviskäM)

if(massa < 1000 ):
    print(f'{massa:0.4f} g')


print(f'Massa nykymitoissa: {massa:0.0f} kg {massa:0.4f}')


