import numpy as np

np.random.seed(42) # Den Seed auf 42 legen, damit die Zahlen immer gleich bleiben
arr = np.random.randint(0, 50, size=(5, 5)) # den Random Array erstellen
print("Original:")
print(arr)
print("") # Leerzeile für Übersichtlichkeit

arr_größer_als_25 = arr[arr > 25] # neuer Array mit allen Werten, die über 25 sind
print(f"alle Werte größer als 25: {arr_größer_als_25}")
print("") # Leerzeile für Übersichtlichkeit

ohne_unter_10 = np.where(arr > 10, arr, -1) # Die Werte dort mit -1 ersetzten, wo sie kleiner als 10 sind
print("Array mit -1:")
print(ohne_unter_10)
print("") # Leerzeile für Übersichtlichkeit

count = len(arr[(arr >= 20) & (arr <= 30)]) # mit hilfe der len Funtion die Länge des neuen arrays finden, der nur Werte zwischen 20 und 30 inklusive behält.
count = np.count_nonzero((arr >= 20) & (arr <= 30)) # Verbesserung von Copilot, mehr Numpyisch
print(f"Anzhal zwischen 20 und 30: {count}")