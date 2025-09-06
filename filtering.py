import numpy as np

# Filtering = Refers to the process of selecting elemts from an array that match a given condition

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65], 
                 [29, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[ages >= 65]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]

print(teenagers)
print(adults)
print(seniors)
print(evens)
print(odds)

new_adults = np.where(ages >= 18, ages, 0)

print(new_adults)
