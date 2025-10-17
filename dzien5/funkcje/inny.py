from funkcje import pole_prostokata

pole_pole = pole_prostokata(10, 5)
print('wynik ostateczny:', pole_pole)

input('ciąg dalszy nastąpi')

from dzien4.dane_z_sieci.waluty5_przelicznik_inaczej import pobierz_tabele

print('funkcja zaimportowana')
tabela = pobierz_tabele()
print(tabela["no"])
print(tabela["rates"][1])

