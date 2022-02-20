#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# -----------------------------------
# # Autor: Mikołaj Henzel, 2022
# -----------------------------------

from tkinter import *
from algorytmy.bubbleSort import bubble_sort
from algorytmy.cocktailSort import cocktail_sort
from algorytmy.heapSort import heap_sort
from algorytmy.mergeSort import merge_sort
from algorytmy.quickSort import quick_sort
from algorytmy.radixSort import radix_sort

from kolory.colors import *
import time
# import winsound

def run(tytul, data, x):

    # Uruchomienie instancji okna
    window = Tk()

    # Rysowanie słupków 

    def drawData(data, colorArray):
        canvas.delete("all")
        canvas_width = 800
        canvas_height = 400
        x_width = canvas_width / (len(data) + 1)
        offset = 4
        spacing = 1
        normalizedData = [i / max(data) for i in data]

        for i, height in enumerate(normalizedData):
            x0 = i * x_width + offset + spacing
            y0 = canvas_height - height * 390
            x1 = (i + 1) * x_width + offset
            y1 = canvas_height
            canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        window.update()

    def generuj():
        start = time.time()
        if x==1:
            bubble_sort(data, drawData, window)
        elif x==2:
            merge_sort(data, 0, len(data)-1, drawData, window),
        elif x==3:
            quick_sort(0, len(data)-1, data, drawData, window),
        elif x==4:
            radix_sort(data, drawData, window),
        elif x==5:
            cocktail_sort(data, drawData, window),
        elif x==6:
            heap_sort(data, drawData, window),
        end = time.time()
        l1.configure(text="Czas: " + str(end-start) + " sekund")
        # # Odtwarzanie dźwięku po przesortowaniu (działa tylko na Windowsie)
        # winsound.PlaySound('dzwieki/dzwiek.wav', winsound.SND_FILENAME)

    # Konfiguracja okna

    window.title("Sortowanie " + tytul + "  |  Mikołaj Henzel")
    window.maxsize(1000, 700)
    window.config(bg = '#eb4034')

    UI_frame = Frame(window, width= 900, height=300, bg=WHITE)
    UI_frame.grid(row=0, column=0, padx=10, pady=5)

    l1 = Label(UI_frame, text="Mierzenie czasu...", bg=WHITE)
    l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)

    b3 = Button(UI_frame, text="Start", command=generuj, bg=LIGHT_GRAY)
    b3.grid(row=2, column=0, padx=5, pady=5)

    canvas = Canvas(window, width=800, height=400, bg='#f23084')
    canvas.grid(row=1, column=0, padx=10, pady=5)

    drawData(data, ['#9248e3' for x in range(len(data))])

    # Uruchomienie okna
    window.mainloop()