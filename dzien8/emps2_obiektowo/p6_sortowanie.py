# Sortujemy pracowników malejąco wg pensji
from emp import wczytaj

emps = wczytaj('emps.csv')

# metoda .sort modyfikuje kolejność wewnątrz listy
emps.sort(key=lambda emp: emp.salary, reverse=True)

# funkcja sorted nie modyfikuje listy, tylko tworzy nową posortowaną jako swój wynik
# posortowana = sorted(emps, key=lambda emp: emp.salary, reverse=True)

for emp in emps:
    print(emp)

print()
print('Najbiedniejszy:', emps[-1])
print('Najbogatszy:', emps[0])
