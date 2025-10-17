import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mbox

FONT = ('Arial', 30, 'bold')

okno = tk.Tk()
okno.title('Kalkulator')
okno.geometry('800x400')

pierwszaLiczba = tk.Entry(master=okno, font=FONT, bg='white')
pierwszaLiczba.pack()

drugaLiczba = tk.Entry(master=okno, font=FONT, bg='white')
drugaLiczba.pack()

listaDzialan = ttk.Combobox(master=okno, values=['+', '-', '*', '/', '^'],
                            justify='center', font=FONT)
listaDzialan.pack()

button = tk.Button(master=okno, text='Oblicz', font=FONT)
button.pack()

labelWynik = tk.Label(master=okno, text='', fg='blue', font=FONT)
labelWynik.pack()

def oblicz():
    try:
        liczba1 = float(pierwszaLiczba.get())
        liczba2 = float(drugaLiczba.get())
        dzialanie = listaDzialan.get()
        match dzialanie:
            case '+': wynik = liczba1 + liczba2
            case '-': wynik = liczba1 - liczba2
            case '*': wynik = liczba1 * liczba2
            case '/': wynik = liczba1 / liczba2
            case '^': wynik = liczba1 ** liczba2
            case _  : wynik = 0
        labelWynik.configure(text=str(wynik), fg='blue')
    except Exception as e:
        labelWynik.configure(text='błąd', fg='red')
        # mbox.showinfo('Błąd', f'Mamy problem\n{e}')
        # mbox.showerror('Błąd', f'Mamy problem\n{e}')

button.config(command=oblicz)

okno.mainloop()
