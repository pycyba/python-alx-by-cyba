import os
import glob
# Lista plików w bieżącym katalogu. To też obejmie podkatalogi i różne pliki specjalne.
lista = os.listdir()
print(lista)
print()

# Można wskazać konkretny katalog do sprawdzenia
#katalog = r'D:\3_Prywatne_Rzeczy\Wydarzenia\30_Cyby_i_Toma'
katalog = r'..'
print(f'Pliki w katalogu {katalog}:')
for plik in os.listdir(katalog):
    print(f'- {plik}')
print()

# glob obsluga wzorcow zawieraajch symbole * i ?
pliky_py = glob.glob('*.py')
print(pliky_py)


pliky_csv = glob.glob('../*/*/.csv')
print(pliky_csv)


print(os.listdrives())

print