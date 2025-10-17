import tkinter as tk

FONT = ('Arial', 30, 'bold')

okno = tk.Tk()
okno.title('Kalkulator')
okno.geometry('800x400')

pierwszaLiczba = tk.Entry(okno, font=FONT, bg='white')
pierwszaLiczba.pack()

drugaLiczba = tk.Entry(okno, font=FONT, bg='white')
drugaLiczba.pack()

button = tk.Button(master=okno, text='Oblicz', font=FONT)
button.pack()

labelWynik = tk.Label(master=okno, text='', fg='blue', font=FONT)
labelWynik.pack()

def oblicz():
    liczba1 = float(pierwszaLiczba.get())
    liczba2 = float(drugaLiczba.get())
    wynik = liczba1 + liczba2
    labelWynik.configure(text=wynik)

button.config(command=oblicz)

okno.mainloop()
