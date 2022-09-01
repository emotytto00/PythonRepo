import sys

try:
    lista = []
    while True:
        lista.append(int(input('Anna luku: ')))
except ValueError:
    print('Toiminta lopetettu')
    lista.sort()
    print('Suurin numero oli', max(lista), 'Pienin numero oli', min(lista))
    sys.exit(0)
