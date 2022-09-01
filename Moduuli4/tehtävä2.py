kerrat = 1

while kerrat >= 1:
    tuuma = float(input('Syötä tuumat'))
    if tuuma >= 0:
        print(f'Tuumat senttimetreinä {tuuma*2.54}')
    else:
        print('negatiivinen luku')
        kerrat = kerrat -1
