def aaa(x):
    print(x*x)


def bbb(x):
    return x*x


from tkinter import messagebox, simpledialog

x = simpledialog.askinteger('Pytanko a', 'Podaj liczbę')
messagebox.showinfo('Odpowiedź', f'{x}² = {aaa(x)}')

x = simpledialog.askinteger('Pytanko b', 'Podaj liczbę')
messagebox.showinfo('Odpowiedź', f'{x}² = {bbb(x)}')
