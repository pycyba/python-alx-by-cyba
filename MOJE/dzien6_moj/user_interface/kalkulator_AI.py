import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mbox

FONT = ('Arial', 30, 'bold')

okno = tk.Tk()
okno.title('Kalkulator')
okno.geometry('800x600')
okno.resizable(False, False)

# Frame dla lepszego układu
frame = tk.Frame(okno, padx=20, pady=20)
frame.pack(expand=True)

tk.Label(frame, text='Liczba 1:', font=('Arial', 16)).pack(pady=(0, 5))
pierwszaLiczba = tk.Entry(frame, font=FONT, bg='white', justify='center')
pierwszaLiczba.pack(pady=(0, 15))

tk.Label(frame, text='Liczba 2:', font=('Arial', 16)).pack(pady=(0, 5))
drugaLiczba = tk.Entry(frame, font=FONT, bg='white', justify='center')
drugaLiczba.pack(pady=(0, 15))

tk.Label(frame, text='Działanie:', font=('Arial', 16)).pack(pady=(0, 5))
listaDzialan = ttk.Combobox(frame, values=['+', '-', '*', '/', '^'],
                            justify='center', font=FONT, state='readonly', width=5)
listaDzialan.current(0)
listaDzialan.pack(pady=(0, 15))

button = tk.Button(frame, text='Oblicz', font=FONT, bg='#4CAF50', fg='white',
                   cursor='hand2', relief='raised', bd=3)
button.pack(pady=(0, 15))

labelWynik = tk.Label(frame, text='Wynik: ', fg='blue', font=FONT)
labelWynik.pack()


def oblicz(event=None):
    try:
        liczba1 = float(pierwszaLiczba.get())
        liczba2 = float(drugaLiczba.get())
        dzialanie = listaDzialan.get()

        if dzialanie == '/' and liczba2 == 0:
            raise ZeroDivisionError("Nie można dzielić przez zero")

        operacje = {
            '+': liczba1 + liczba2,
            '-': liczba1 - liczba2,
            '*': liczba1 * liczba2,
            '/': liczba1 / liczba2,
            '^': liczba1 ** liczba2
        }

        wynik = operacje.get(dzialanie, 0)
        labelWynik.configure(text=f'Wynik: {wynik:.6g}', fg='blue')

    except ValueError:
        labelWynik.configure(text='Błąd: Wprowadź liczby', fg='red')
    except ZeroDivisionError as e:
        labelWynik.configure(text=f'Błąd: {e}', fg='red')
    except Exception as e:
        labelWynik.configure(text=f'Błąd: {e}', fg='red')


button.config(command=oblicz)

# Obsługa Enter
okno.bind('<Return>', oblicz)
pierwszaLiczba.focus()

okno.mainloop()