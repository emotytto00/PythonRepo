import mysql.connector

def haeLentokenttä(ICAO):
    tuple = (ICAO,)
    sql = '''SELECT Name, municipality FROM airport
    WHERE ident = %s;'''
    kursori = yhteys.cursor()
    kursori.execute(sql, tuple)
    tulos = kursori.fetchone()
    if tulos is not None:
        print(tulos[0], tulos[1])

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='DonGio024',
         autocommit=True
         )
haeLentokenttä(input('Kerro lentokentän ICAO-koodi: '))
