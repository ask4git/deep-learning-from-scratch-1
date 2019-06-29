
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

if __name__ == '__main__':
    # data set
    x = np.arange(0, 6, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)

    # data visualization
    plt.plot(x, y1, label="sin")
    plt.plot(x, y2, linestyle="--", label="cos")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('sin & cos')
    plt.legend()
    plt.show()

    # read image
    img = imread('..\\resource\\TensorFlowLogo.jpg')

    plt.imshow(img)
    plt.show()
