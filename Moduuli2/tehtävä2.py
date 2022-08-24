print('Hello Johannes')
#print('Eka', end='ö')
#print('Toka')
print('Tämä ohjelma muuntaa kilokalorit jouleksi')

kaloritMJ = input('Anna energiasisltö kilokaloreina:')
print('Muunnetaan ' + kaloritMJ + ' kilokaloria kilojouleiksi')
kalorit = float(kaloritMJ)
#kilojoulet = 4.184 * kalorit

print(f'Se on {kaloritMJ*4.184:.0f} kilojoulea.')