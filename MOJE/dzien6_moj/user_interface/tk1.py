import tkinter as tk

okno = tk.Tk()
okno.geometry('600x600')
okno.title('Przykładowa apka')

label1 = tk.Label(master=okno, text='Pierwszy tekst',
                  font='Arial 30 bold',
                  foreground='blue')
label1.pack()

label2 = tk.Label(master=okno, text='Drugi tekst',
                  font='Times 24 italic',
                  foreground='#660044'
                  )
label2.pack()
button_font = ('Comic Sans MS', 40, 'bold')
button1 = tk.Button(master=okno, text='Guzik 1',font=button_font)
button1.pack()

button2 = tk.Button(master=okno, text='Guzik 2', font=button_font)
button2.pack()

#oporcz tej mozliwosci podania atrybutow podczas tworzenia komponentu,
#mozna pozniej zmienic ustawienia za pomoca configure
button1.configure(background='yellow')
okno.mainloop()
