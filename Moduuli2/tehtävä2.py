#print('Hello Johannes')
#print('Eka', end='ö')
#print('Toka')
#print('Tämä ohjelma muuntaa kilokalorit jouleksi')
import math

#print('Muunnetaan ' + kaloritMJ + ' kilokaloria kilojouleiksi')
#kalorit = float(kaloritMJ)
#kilojoulet = 4.184 * kalorit

#print(f'Se on {kaloritMJ*4.184:.0f} kilojoulea.')
säde_str = input('Mikä on ympyrän säde?')
säde = float(säde_str)
print(f'Pinta-ala on {float(math.pi*math.pi)/säde} ')