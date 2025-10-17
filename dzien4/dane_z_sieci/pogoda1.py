import requests

lat, lon = 52, 21
url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min&hourly=temperature_2m,relative_humidity_2m,precipitation&current=temperature_2m,relative_humidity_2m'

dane = requests.get(url).json()
print(dane)

print(dane["current"])
print('bieżąca temperatura:', dane["current"]["temperature_2m"])
print('bieżąca wilgotność:', dane["current"]["relative_humidity_2m"])
print()

# print(dane["daily"])

# for tuple in zip(*dane["daily"].values()):
#     print(*tuple)

daily = dane["daily"]

for time, tmin, tmax in zip(daily["time"], daily["temperature_2m_min"], daily["temperature_2m_max"]):
    print(f'Dnia {time} przewidujemy temperaturę od {tmin} do {tmax}')


