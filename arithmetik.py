import numpy as np

# Scalar arithmetic

array = np.array([1, 2, 3])

print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)
print("")
# Vectorized math funcs
array = np.array([1.5453, 2.321441513, 3.4124642629888709])

print(np.sqrt(array))
print(np.round(array))
print(np.floor(array)) # immer runter runden
print(np.ceil(array)) # immer hoch runden
print(np.pi)

radii = np.array([1, 2, 3])

print(np.pi * radii ** 2)

print("")
# Element whise arithemtic

array1 = np.array([1, 2, 3])
array2 = np.array([1, 5, 6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)

print("")
# Comparision operators

scores = np.array([91, 55, 100, 73, 82, 64])

print(scores >= 60)
scores[scores < 60] = 0
print(scores)