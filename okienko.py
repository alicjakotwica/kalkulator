from tkinter import *
import tkinter.ttk as ttk
from kalkulator import *


okno= Tk()

etykieta1=Label(okno, text ="Wpisz pierwszą liczbę:")
etykieta1.grid(row=0,column=0)

operacje=('+', '-', '*', '/')

cb_value = StringVar()
combobox = ttk.Combobox(okno, textvariable = cb_value)
combobox.grid(row=1,column=1)
combobox['values'] = operacje
combobox.current(0)

etykieta2=Label(okno, text ="Wpisz pierwszą liczbę:")
etykieta2.grid(row=0,column=2)

etykieta3=Label(okno, text ="Wynik:")
etykieta3.grid(row=0,column=3)

pole1 = Entry(okno)
pole1.grid(row=1,column=0)

pole2 = Entry(okno)
pole2.grid(row=1,column=2)

etykieta3=Label(okno, text ="")
etykieta3.grid(row=1,column=3)


def wypisz(event):
    jeden= float(pole1.get())
    dwa= float(pole2.get())
    wybor=cb_value.get()

    if wybor==operacje[0]:
        wynik=dodawanie(jeden,dwa)
    elif wybor==operacje[1]:
        wynik=odejmowanie(jeden,dwa)
    elif wybor==operacje[2]:
        wynik=mnozenie(jeden,dwa)
    else:
        wynik=dzielenie(jeden,dwa)
    
    etykieta3.config(text=str(wynik))


def usun(event):
    pole1.delete(0, END)
    pole2.delete(0, END)
    etykieta3.config(text="")

przycisk = Button(okno, text="Chce wynik!")
przycisk.grid(row=2, columnspan = 5, sticky=E+N+W+S)
przycisk.bind("<Button-1>",wypisz)

przycisk2 = Button(okno, text="Wyzeruj pola")
przycisk2.bind("<Button-1>",usun)
przycisk2.grid(row=3, columnspan = 5, sticky=E+N+W+S)

okno.mainloop()