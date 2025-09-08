import numpy as np

a = np.arange(1, 13)

newarr = a.reshape(3, 4)
print(f"3x4: \n{newarr}")

splitarr = np.array_split(a, 2)
print(splitarr)