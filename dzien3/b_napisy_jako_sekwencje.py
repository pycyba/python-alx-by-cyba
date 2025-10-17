napis = input('Podaj napis:\n')

print('Pierwszy znak:', napis[0])
print('Ostatni znak:', napis[-1])
print('Co drugi znak:', napis[::2])
print('Napis od tyłu:', napis[::-1])
print()
print('Pętla for dla wszystkich znaków po kolei:')

for znak in napis:
    # print(znak)
    print(f'kolejny znak to "{znak}", jego kodem jest {ord(znak)}')

