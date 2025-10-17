from emp import wczytaj

emps = wczytaj('emps.csv')

# Wypisz imię, nazwisko i miasto
for emp in emps:
    print(emp.first_name, emp.last_name, 'z miasta', emp.city)


# Zadanka do zrobienia w oparciu o podejście obiektowe:
# p2_wypisz_bogatych - wypisz tylko tych pracowników, którzy zarabiają ≥ 10 tys
# p3_srednia_wszystkich
# p4_srednia_jeden_job

# p5_min_max - wypisz dane pracownika, który zarabia najwięcej, oraz pracownika, który zarabia najmniej
# (co najmniej imię, nazwisko i pensję, ale można też 'cały obiekt')

# grupowanie - dla każdego joba oblicz średnią pensję
