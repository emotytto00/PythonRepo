import mysql.connector
from geopy import distance

def haeLentokenttä(ICAO):
    sql = f'''SELECT latitude_deg, longitude_deg FROM airport
    WHERE ident = "{ICAO}"'''
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    if tulos is not None:
        return tulos

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='DonGio024',
         autocommit=True
         )
ekaKenttä = haeLentokenttä(input('Syötä ensimmäinen ICAO-koodi: '))
tokaKenttä = haeLentokenttä(input('Syötä toinen ICAO-koodi: '))

print(f'Kenttien välinen matka on {int(distance.distance(ekaKenttä, tokaKenttä).km)} kilometreissä.')