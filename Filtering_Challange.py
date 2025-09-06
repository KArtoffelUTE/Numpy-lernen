import numpy as np

data = np.array([
    [5,  2,  9,  1],
    [8,  7,  3,  4],
    [6, 10, 12, 11]
])

mean = np.mean(data)
print(f"Mittelwert: {np.round(mean, 3)}")

print(f"Gefiltert: {data[data > mean]}")

sort = data[data > mean]
print(f"Sortiert: {sort[::-1]}")