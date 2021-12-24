import numpy as np
import cv2

from convergence_mapping import mandelbrot_iterator, gen_convergence_map
from img_generators import nrootr_gradient

# SETUP

# convergence-map generation
size = (1000, 2000)
iterations = 100
bound = 10
real_axis = (-3, 1)
imag_axis = (-1, 1)

# image generation
order = 2
destination = 'tmp/mandelbrot.png'
convergence_color = (0, 0, 0)

# rectangle selection
right_down = np.array([int(size[1] / 2), int(size[0] / 2)], dtype=int)
left_up = np.array([- int(size[1] / 2), - int(size[0] / 2)], dtype=int)
center = np.array([int(size[1] / 2), int(size[0] / 2)], dtype=int)
zoom = 0.5
edit = False
pt1 = (center + zoom * left_up).astype(int)
pt2 = (center + zoom * right_down).astype(int)

# generate convergence map and image
conv_map, gaussian = gen_convergence_map(mandelbrot_iterator, size, iterations=iterations, bound=bound,
                                         real_axis=real_axis,
                                         imag_axis=imag_axis, ret_gaussian=True)
out = nrootr_gradient(conv_map, order=order, destination=destination, convergence_color=convergence_color, ret=True)

original = out.copy()

# exploration loop
while True:

    cv2.imshow('fractal', out)
    key = cv2.waitKey(0)
    if key == ord('q'):
        exit(0)

    elif key == ord('s'):
        # save image

        cv2.destroyAllWindows()

        destination = input('specify destination path (without ending):')
        destination += '.png'
        cv2.imwrite(destination, out)
        print('continue exploring?')
        if input('[Y/n]') == 'n':
            exit(0)

    elif key == ord('e'):
        # toggle edit mode
        if edit:
            edit = False
            out = original.copy()
        else:
            edit = True
            cv2.rectangle(out, pt1, pt2, (0, 0, 255), 3, lineType=cv2.LINE_AA)

    elif key == 13:  # enter
        # confirm selection if in edit mode
        cv2.destroyAllWindows()

        gaussian_pnt1 = gaussian[pt1[1]][pt1[0]]
        gaussian_pnt2 = gaussian[pt2[1]][pt2[0]]

        real_interval_size = abs(gaussian_pnt1.real - gaussian_pnt2.real)
        real_start = min(gaussian_pnt1.real, gaussian_pnt2.real)
        imag_interval_size = abs(gaussian_pnt1.imag - gaussian_pnt2.imag)
        imag_start = min(gaussian_pnt1.imag, gaussian_pnt2.imag)

        real_axis = (real_start, real_start + real_interval_size)
        imag_axis = (imag_start, imag_start + imag_interval_size)

        conv_map, gaussian = gen_convergence_map(mandelbrot_iterator, size, iterations=iterations, bound=bound,
                                                 real_axis=real_axis,
                                                 imag_axis=imag_axis, ret_gaussian=True)
        out = nrootr_gradient(conv_map, order=order, destination=destination, convergence_color=convergence_color,
                              ret=True)

        # re-initialize rectangle
        right_down = np.array([int(size[1] / 2), int(size[0] / 2)], dtype=int)
        left_up = np.array([- int(size[1] / 2), - int(size[0] / 2)], dtype=int)
        center = np.array([int(size[1] / 2), int(size[0] / 2)], dtype=int)
        zoom = 0.5
        edit = False
        original = out.copy()

    elif key == 81:  # left-arrow
        # move rectangle if in edit mode
        center[0] -= 10

        out = original.copy()

        # draw rectangle
        pt1 = (center + zoom * left_up).astype(int)
        pt2 = (center + zoom * right_down).astype(int)

        cv2.rectangle(out, pt1, pt2, (0, 0, 255), 3, lineType=cv2.LINE_AA)


    elif key == 82:  # up-arrow
        # move rectangle if in edit mode
        center[1] -= 10

        out = original.copy()

        # draw rectangle
        pt1 = (center + zoom * left_up).astype(int)
        pt2 = (center + zoom * right_down).astype(int)

        cv2.rectangle(out, pt1, pt2, (0, 0, 255), 3, lineType=cv2.LINE_AA)


    elif key == 83:  # rightarrow
        # move rectangle if in edit mode
        center[0] += 10

        out = original.copy()

        # draw rectangle
        pt1 = (center + zoom * left_up).astype(int)
        pt2 = (center + zoom * right_down).astype(int)

        cv2.rectangle(out, pt1, pt2, (0, 0, 255), 3, lineType=cv2.LINE_AA)


    elif key == 84:  # down-arrow
        # move rectangle if in edit mode
        center[1] += 10

        out = original.copy()

        # draw rectangle
        pt1 = (center + zoom * left_up).astype(int)
        pt2 = (center + zoom * right_down).astype(int)

        cv2.rectangle(out, pt1, pt2, (0, 0, 255), 3, lineType=cv2.LINE_AA)

    elif key == ord('+'):
        # zoom in if in edit mode
        zoom -= 0.05

        out = original.copy()

        # draw rectangle
        pt1 = (center + zoom * left_up).astype(int)
        pt2 = (center + zoom * right_down).astype(int)

        cv2.rectangle(out, pt1, pt2, (0, 0, 255), 3, lineType=cv2.LINE_AA)

    elif key == ord('-'):
        # zoom out if in edit mode
        zoom += 0.05

        out = original.copy()

        # draw rectangle
        pt1 = (center + zoom * left_up).astype(int)
        pt2 = (center + zoom * right_down).astype(int)

        cv2.rectangle(out, pt1, pt2, (0, 0, 255), 3, lineType=cv2.LINE_AA)
    else:
        # print 'incorrect input' on image
        pass
