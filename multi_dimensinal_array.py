#Numpy Arrays
import numpy as np

array_0d = np.array('A') # 0 Dimensional
print(array_0d.ndim)

array_1d = np.array(['A', 'B']) # 1 Dimensional
print(array_1d.ndim)

array_2d = np.array([['A', 'B'], ['C', 'D']]) # 2 Dimensional
print(array_2d.ndim)

array_3d = np.array([[['A', 'B'], ['C', 'D'], ['E', 'F'],
                      ['G', 'H'], ['I', 'J'], ['K', 'L'],
                      ['M', 'N'], ['O', 'P'], ['Q', 'R']]]) # 3 Dimensional
print(array_3d.ndim)