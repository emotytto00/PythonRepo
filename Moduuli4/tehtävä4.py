import random
toistot = 1
arvoitus = random.randint(1,10)


while toistot == 1:
    arvaus = int(input('Arvaa oikea luku 1-10 väliltä'))
    if arvaus == arvoitus:
        break
    elif arvaus > arvoitus:
        print('Liian iso luku')
    elif arvaus < arvoitus:
        print('Liian pieni luku')
print('Oikein meni')