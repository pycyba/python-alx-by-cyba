import subprocess

print('Początek Pythona')

# Program bez żadnych argumentów można uruchomić tak:
subprocess.run('ls')
# subprocess.run('kcalc')
# subprocess.run('calc.exe')
# subprocess.run(r'C:\Program Files\GIMP 2\bin\gimp-2.10.exe')

# W tej wersji program wypisuje swoje wyśjcie na standardowe wyjście tego procesu Pythona.
# (Python nie przechwytuje wyjścia tego procesu, tylko "wypuszcza je na zewnątrz").

print('Koniec Pythona')
