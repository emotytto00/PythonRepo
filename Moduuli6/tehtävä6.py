def hinta(halkCM, hintEUR):
    return float(hintEUR / (halkCM * 0.01))
halk1 = float(input('Anna 1. halkaisija cm: '))
hint1 = float(input('Anna 1. hinta eur: '))
halk2 = float(input('Anna 2. halkaisija cm: '))
hint2 = float(input('Anna 2. hinta eur: '))

yksikköhinta = hinta(halk1, hint1)
yksikköhinta2 =  hinta(halk2, hint2)

if yksikköhinta > yksikköhinta2:
    print(f'2. pizza on halvempi: {yksikköhinta2} euroa per neliömetri')
else:
    print(f'1. pizza on halvempi: {yksikköhinta} euroa per neliömetri')