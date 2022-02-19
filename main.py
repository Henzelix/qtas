from tkinter import *
import random

# Tablica z liczbami
data = []

# Wybór algorytmu sortowania
jakiAlgorytm = int(input("Wybierz algorytm:\n1. Bąbelkowe\n2. Przez scalanie"))

# Wybór ilości wylosowanych liczb do podstawienia pod algorytm sortujący
ileLiczb = int(input("Podaj ile liczb chcesz wylosować (od 2 do 1000): "))

# Losowanie liczb i dodanie ich do tablicy
for i in range(ileLiczb):
    wylosowana = random.randint(1,1000)
    data.append(wylosowana)

print(data)

# Uruchomienie okna
window = Tk()

window.title("Wizualizacja sortowania algorytmów")
window.maxsize(1000, 700)
window.config(bg = '#eb4034')

window.mainloop()