import tkinter as tk
import tkinter.messagebox as mbox
import tkinter.ttk as ttk


FONT = ('Arial', 30, 'bold')

okno = tk.Tk()
okno.title('Kalkulator')
okno.geometry('800x400')

pierwszaLiczba = tk.Entry(okno, font=FONT, bg='white')
pierwszaLiczba.pack()

drugaLiczba = tk.Entry(okno, font=FONT, bg='white')
drugaLiczba.pack()


listaDzialan = ttk.Combobox(master=okno, values=["+", "-", "*", "/", "^"], font=FONT)
listaDzialan.pack()


button = tk.Button(master=okno, text='Oblicz', font=FONT)
button.pack()

labelWynik = tk.Label(master=okno, text='', fg='blue', font=FONT)
labelWynik.pack()

def oblicz():
    try:
        liczba1 = float(pierwszaLiczba.get())
        liczba2 = float(drugaLiczba.get())
        wynik = liczba1 + liczba2
        labelWynik.configure(text=str(wynik), fg='blue')
    except Exception as e:
        labelWynik.configure(text='błąd', fg='red')
        # mbox.showinfo('Błąd', f'Mamy problem\n{e}')
        # mbox.showerror('Błąd', f'Mamy problem\n{e}')

button.config(command=oblicz)

okno.mainloop()
