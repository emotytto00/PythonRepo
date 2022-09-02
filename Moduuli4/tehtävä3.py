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

#vaihtoehtoinen ratkaisu
#lukustr = input('Anna luku tai lopeta tyhjällä syötteellä: ')
#while lukustr !="":
#   lukustr = input('Anna seuraava luku tai lopeta tyhjällä: ')
#       luku = float(lukustr)
#           if luku < pienin:
                #pienin = luku
            #if luku> suurin:
            #   suurin = luku
#print(f'Antamistasi luvuista pienin oli {pienin} ja suurin oli {suurin}')