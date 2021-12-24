import numpy as np
import cv2 as cv
from tqdm import tqdm


def mandelbrot_iterator(seed, iterations, bound):
    z = complex(0, 0)
    for i in range(iterations):
        z = z ** 2 + seed
        if abs(z) >= bound:
            return i + 1

    return -1


def gen_convergence_map(iterator, size, real_axis=(-1, 1), imag_axis=(-1, 1), iterations=100, bound=100, ret_gaussian=False):

    # generate the axes from the endpoints
    real_axis = np.linspace(real_axis[0], real_axis[1], size[1])
    imag_axis = np.linspace(imag_axis[0], imag_axis[1], size[0])

    # initialize gaussian plane
    # size refers to size of screen (height, width)
    gaussian = np.zeros(size, dtype='complex')

    # generate gaussian plane
    print('generating gaussian plane...')
    it = np.nditer(gaussian, flags=['multi_index'])
    for x in tqdm(it, total=it.itersize):
        i, j = it.multi_index
        gaussian[i][j] = complex(real_axis[j], imag_axis[-(i + 1)])

    # initialize convergence map
    convergence_map = np.zeros(size, dtype=int)

    # generate convergence map
    print('generating convergence map...')
    it = np.nditer(convergence_map, flags=['multi_index'])
    for x in tqdm(it, total=it.itersize):
        i, j = it.multi_index
        convergence_map[i][j] = iterator(gaussian[i][j], iterations, bound)

    print('done.\n')

    if ret_gaussian:
        return convergence_map, gaussian
    else:
        return convergence_map
