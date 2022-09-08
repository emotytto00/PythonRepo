def gMuunnin(gallonat):
    return gallonat * 3.785

gallonat = float(input('Anna bensan määrä gallonissa: '))

while gallonat >= 0:
    litrat = gMuunnin(gallonat)
    print(litrat)
    gallonat = float(input('Anna uusi bensan määrä gallonissa bro: '))
