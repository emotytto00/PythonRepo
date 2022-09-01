toistot = 1
käyttäjä = 'python'
salasana = 'rules'

while toistot <= 5:
    käy = input('Syötä käyttäjätunnus: ')
    sal = input('Syötä salasana: ')
    if käy == käyttäjä:
        if sal == salasana:
            print('Teretulemast tallinkil')
            break
        else:
            print('Pääsy evätty')
            toistot = toistot +1
    else:
        print('Pääsy evätty')
        toistot = toistot +1

        #vaihtoehtoinen ratkaisu laitettu kommentteihin

#while (käy!=str('python') and sal!=str('rules)'
    #if käy!=str('python') or sal!=str('Rules')
      #  print('Pääsy evätty')
    #käy = input('Anna käyttis')
    #sal = input('Anna salis')
    #print('Tervetuloa)'