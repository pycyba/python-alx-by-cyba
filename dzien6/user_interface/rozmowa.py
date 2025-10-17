import tkinter as tk

root = tk.Tk()

root.title('Rozmowa')
root.geometry('800x600')

label1 = tk.Label(master=root, text='Jak masz na imię?', fg='black', font=('Arial', 24, 'bold'))
label1.pack()

poleTekstowe = tk.Entry(root, font=('Consolas', 24), bg='white')
poleTekstowe.pack()

button1 = tk.Button(master=root, text='OK', font=('Arial', 24, 'bold'))
button1.pack()

label2 = tk.Label(master=root, text='', fg='blue', font=('Arial', 24, 'bold'))
label2.pack()

# Funkcja obsługująca naciśnięcie przycisku, do wykorzystania w command
# nie powinna przyjmować żadnych parametrów
def kliknieto_guzik():
    imie = poleTekstowe.get()
    label2.configure(text=f'Witaj {imie}!', fg='blue')

button1.configure(command=kliknieto_guzik)

# Bardziej ogólnym sposobem wiązania obsługi zdarzeń z komponentami
# jest metoda bind. Są różne rodzaje zdarzeń, '<Return>' oznacza naciśnięcie Enter.
# Funkcja, którą chcemy związać za pomocą bind, ma przyjmować jeden parametr - obiekt zdarzenia.
def nacisnieto_enter(evt):
    imie = poleTekstowe.get()
    label2.configure(text=f'Cześć {imie}!', fg='green')

poleTekstowe.bind('<Return>', nacisnieto_enter)

# tak już nie: poleTekstowe.configure(command=nacisnieto_enter)

root.mainloop()
