import subprocess

# W tej wersji włączymy opcję zbierania outputu - to pozwala odczytać output po zakończeniu procesu.

# Wyjście programu jest zapamiętywane w RAM, a potem można to odczytać.

result = subprocess.run(['python3', '../../w1/petle_wprowadzenie.py'], capture_output=True)

print('Proces zakończony kodem', result.returncode)
print('Output:')
print(result.stdout)
print(result.stderr) # komunikaty o błędach

# to jest "tablica bajtów", a żeby uzyskać wersję string, trzeba zdekodować
string = result.stdout.decode('utf-8')
print('\n\nOutput programu:\n')
print(string)
print('---------')