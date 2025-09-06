import numpy as np

rng = np.random.default_rng(seed = 1) # seed nicht notwendig

print(rng.integers(low=1, high=101, size=(3, 2)) )# high und low nicht notwendig

# floating point numbers
np.random.seed(seed = 1)

print(np.random.uniform(-1, 1, 3))

rng = np.random.default_rng()

array = np.array([1, 2, 3 ,4 ,5])
rng.shuffle(array) #Array Shuffeln
print(array)

fruits = np.array(("appel ", "orange", "Trauben", "Tomaten", "Melon", "banana", "pineappel"))
fruit = rng.choice(fruits, size=(3, 3))
print(fruit)