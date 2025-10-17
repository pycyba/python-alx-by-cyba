import requests

lat, lon = 52, 21

url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min&hourly=temperature_2m,relative_humidity_2m,precipitation&current=temperature_2m,relative_humidity_2m'

dane = requests.get(url).json()
print(dane)

print(dane["current"])
print('biezaca tem')
