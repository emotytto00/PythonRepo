kuha = int(input('Kuhan pituus :'))
sallittuKoko = int(37)
pieniKuhaFunktio = (sallittuKoko - kuha)

if (kuha >= sallittuKoko):
    print('No nyt on kalalla kokoa!')

if (kuha < sallittuKoko):
    print('Kala takas jorpakkoo ja sassii!')
    print('Kuhan on oltava', pieniKuhaFunktio,'cm pidempi, jotta se on sopivan pituinen')
