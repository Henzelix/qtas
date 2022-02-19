from tkinter import *
from algorytmy.bubbleSort import bubble_sort
from kolory.colors import *
import random

# Uruchomienie instancji okna
window = Tk()

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

# Rysowanie słupków 

def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
    window.update_idletasks()

def generuj():
    bubble_sort(data, drawData, 0.001)

# Konfiguracja okna

window.title("Wizualizacja sortowania algorytmów")
window.maxsize(1000, 700)
window.config(bg = '#eb4034')

UI_frame = Frame(window, width= 900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

b3 = Button(UI_frame, text="Start", command=generuj, bg=LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)

canvas = Canvas(window, width=800, height=400, bg='#f23084')
canvas.grid(row=1, column=0, padx=10, pady=5)

drawData(data, ['#9248e3' for x in range(len(data))])

# Uruchomienie okna
window.mainloop()