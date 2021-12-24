import numpy as np
from tqdm import tqdm
import time


test_array = np.zeros((10, 10), dtype='complex')

for i in range(10):
    for j in range(10):
        test_array[i][j] = complex(i, j)

it = np.nditer(test_array, flags=['multi_index'])

for x in it:
    i, j = it.multi_index
    print('normal indicis: {},{}  multi indicis: {},{}'.format(int(x.real), int(x.imag), i, j))
