import mysql.connector
from flask import Flask

app = Flask(__name__)
@app.route('/airport/<ICAO>')
def searchAirport(ICAO):
    tuple = (ICAO,)
    sql = '''SELECT Name, municipality FROM airport
    WHERE ident = %s;'''
    kursori = yhteys.cursor()
    kursori.execute(sql, tuple)
    tulos = kursori.fetchone()
    if tulos is not None:
        answer = {
            "ICAO" : ICAO, "Name" : tulos, "Municipality" : tulos
        }
        return answer
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='DonGio024',
         autocommit=True
         )
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
