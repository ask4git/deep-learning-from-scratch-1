
# -*- coding: utf-8 -*-

import numpy as np

if __name__ == '__main__':
    # data format
    # =================================
    # scalar
    s = np.array([1.])

    # vector
    v = np.array([1., 2., 3.])

    # matrix
    m = np.array([[1., 2., 3.],
                  [1., 2., 3.]])

    # 3-tensor
    tensor_3 = np.array([[[1., 2., 3.],
                         [1., 2., 3.]],

                        [[1., 2., 3.],
                        [1., 2., 3.]],

                        [[1., 2., 3.],
                        [1., 2., 3.]]])
    # =================================

    print(m)
    print(type(m))

    # shape of tensor
    print(m.shape)

    # data type
    print(m.dtype)

    # broadcast example
    # =================================
    a = np.array([[1., 2.], [3., 4.]])
    b = np.array([10, 20])
    print("broadcast example")
    print(a * b)
    # =================================

    # how to access numpy elements
    # =================================
    x = np.array([[51, 55], [14, 19], [0, 4]])

    # accessing with indexes
    print(x)
    print(x[0])
    print(x[0][1])

    # accessing with loops
    for row in x:
        print(row)

    # flatten
    x = x.flatten()
    print(x)    # [51 55 14 19  0  4]

    print(x[np.array([0, 2, 4])])   # [51 14  0]

    print(x > 15)   # [ True  True False  True False False]

    print(x[x > 15])    # [51 55 19]
    # =================================
