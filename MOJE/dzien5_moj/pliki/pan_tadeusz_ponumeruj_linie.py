"""
Wypisz na ekran wszystkie Linie Pana Tadeusza ponumerowane rosnaca od 1

"""

# with open('pan_tadeusz.txt', 'r', encoding='UTF-8') as wejscie:
#     b = 0
#     for i in wejscie:
#         b += 1
#         print( b, i.rstrip())


"""Ponumerowane LINIE PT zapisz do nowego pliku, np """
#
# with open('pan_tadeusz.txt', 'r', encoding='UTF-8') as wejscie:
#     wyjscie = open('ponumerowane.txt', 'w', encoding='utf-8')
#     b = 0
#     for i in wejscie:
#         if i.strip() == '':
#             continue
#         else:
#             b += 1
#             print( b, i.rstrip(), file=wyjscie)
#     wyjscie.close()
z
with open('pan_tadeusz.txt', 'r', encoding='UTF-8') as wejscie:
    with  open('ponumerowane.txt', 'w', encoding='utf-8') as wyjscie:
        b = 0
        for i in wejscie:
            if i.strip() == '':
                continue
            else:
                b += 1
                print(b, i.rstrip(), file=wyjscie)
