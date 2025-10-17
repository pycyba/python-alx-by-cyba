import os
import glob
import shutil

print('Rodzaj systemu:', os.name,  os.uname())
print('Nazwa użytkownika:', os.getlogin())
print()
print('Zmienne środowiskowe:')
for zmienna, wartosc in os.environ.items():
    print(f'{zmienna} = {wartosc}')

print()

# Lista plików w bieżącym katalogu. To też obejmie podkatalogi i różne pliki specjalne.
lista = os.listdir()
print(lista)
print()

# Można wskazać konkretny katalog do sprawdzenia
katalog = '..'
# katalog = '/home/patryk/sklep/foto'
# katalog = r'C:\Users\kurs\Desktop'
print(f'Pliki w katalogu {katalog}:')
for plik in os.listdir(katalog):
    print(f'- {plik}')
print()

# glob - obsługa wzorców zawierających symbole * i ?
pliki_py = glob.glob('*.py')
print(pliki_py)

pliki_csv = glob.glob('../*/*.csv')
print('csv dzisiaj:', pliki_csv)
print()

pliki_csv = glob.glob('**/*.csv', root_dir='../../', recursive=True)
print('csv wszystkie:', pliki_csv)
print()



#print('listdrives:', os.listdrives())

print(shutil.disk_usage('.'))
