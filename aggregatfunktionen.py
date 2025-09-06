import numpy as np

# Aggregate Functions = summarize data and typically return a single value


array = np.array([[1, 2, 3, 4, 5], 
                  [6, 7, 8, 9, 10]])

print(np.sum(array))  # Die Summe
print(np.mean(array)) # Der Durschnitt
print(np.std(array)) # The messure of spred?
print(np.var(array)) # Die Varianten der ² von std
print(np.min(array)) # Minimal
print(np.max(array)) # Maxiaml
print(np.argmin(array)) # Die Position des Minimal Werts
print(np.argmax(array)) # Die Position des Maximal Werts

print(np.sum(array, axis= 1)) # summmierd die posiotiojn ngöeich, lass laufen und schaue


