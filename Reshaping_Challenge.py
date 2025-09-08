import numpy as np

a = np.arange(1, 13)

newarr = a.reshape(3, 4)
print(f"3x4: \n{newarr}\n")

left = newarr[:, :2]
right = newarr[:, 2:]
print("Split:")
print(left)
print(right)
print("")

stackarr = a.reshape(6, 2)
print(f" Gestackt: \n {stackarr}")