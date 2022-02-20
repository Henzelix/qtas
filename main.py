#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# -----------------------------------
# Autor: Mikołaj Henzel, 2022
# -----------------------------------

from uruchom import run
import random

tytuly = [
    "Bąbelkowe",
    "Przez scalanie"
]

x = 1

# Tablica z liczbami
data = []

dane = []


# Wybór ilości wylosowanych liczb do podstawienia pod algorytm sortujący
ileLiczb = int(input("Podaj ile liczb chcesz wylosować (od 2 do 1000): "))

# Losowanie liczb i dodanie ich do tablicy
for i in range(ileLiczb):
    wylosowana = random.randint(1,1000)
    data.append(wylosowana)

print(data)


while(x!=0):
    # Wybór algorytmu sortowania
    x = int(input("Wybierz algorytm:\n0. Zamknij\n1. Bąbelkowe\n2. Przez scalanie\n\n"))

    if(x!=0):
        dane = data.copy()
        print(data)
        run(tytuly[x-1], dane)
    else:
        x = 0
