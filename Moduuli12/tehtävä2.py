import requests
import json

#ohjelma
APIkey = 'fb0e15b1ca7ed0a91fcd6d1a7c89b810'
hakusana = input('Anna jokin paikkakunta: ')


pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q=%7Bhakusana%7D&appid=%7BAPIkey%7D"
vastaus = requests.get(pyyntö).json()



#weather
vastaus_sää = vastaus['weather'][0]['main']
print(f'Current weather in {hakusana}: {vastaus_sää}')

#Temperaturem 1 kelvin = -273,15
tocelsius = 273.15
vastaus_temp = vastaus['main']['temp']
print(f'Currently temperature in {hakusana}: {round((vastaus_temp-tocelsius), 1)} celsius')