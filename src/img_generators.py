import numpy as np
import cv2
from tqdm import tqdm


def nrootr_gradient(conv_map, destination=None, convergence_color=(0, 0, 0), order=2, ret=False, view=False):
    print('generating image using nroot gradient...')

    if isinstance(conv_map, str):
        conv_map = np.load(conv_map)
        print('loaded convergence map from file.')

    # find max value in convergence map
    print('identifying max divergence value...')
    max_value = 0

    it = np.nditer(conv_map)
    for x in tqdm(it, total=it.itersize):
        if x >= max_value:
            max_value = x

    print('max divergence value is {0}'.format(max_value))

    # initialize image
    shape = (conv_map.shape[0], conv_map.shape[1], 3)
    color_map = np.zeros(shape, dtype='uint8')

    print('generating image...')

    # generate image
    it = np.nditer(conv_map, flags=['multi_index'])
    for x in tqdm(it, total=it.itersize):
        i, j = it.multi_index
        if x == -1:
            color_map[i][j] = convergence_color
        else:
            hue = 255 * np.power(conv_map[i][j] / max_value, 1 / order)
            color_map[i][j] = (hue, 255, 255)

    # convert to BGR
    print('converting HSV to BGR...')
    color_map = cv2.cvtColor(color_map, cv2.COLOR_HSV2BGR)

    # view image
    if view:
        print('done.')
        cv2.imshow('fractal', color_map)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    if destination is not None:
        cv2.imwrite(destination, color_map)

    if ret:
        return color_map
