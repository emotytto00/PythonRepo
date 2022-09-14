import mysql.connector

def haeLentokenttä(maak, tyyppi):
    tuple = (maak, tyyppi)
    sql = '''SELECT COUNT(type) FROM airport
    WHERE iso_country = %s
    AND type = %s;'''
    kursori = yhteys.cursor()
    kursori.execute(sql, tuple)
    tulos = kursori.fetchone()
    return tulos

def haeTyypit():
   sql = '''SELECT DISTINCT type FROM airport;'''
   kursori = yhteys.cursor()
   kursori.execute(sql, )
   tulos = kursori.fetchall()
   return tulos

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='DonGio024',
         autocommit=True
         )
käyttäjä = input('Kerro lentokentän maakoodi: ')

tyypit = haeTyypit()
for tyyppi in tyypit:
    print(haeLentokenttä(käyttäjä, tyyppi[0]), tyyppi[0])
