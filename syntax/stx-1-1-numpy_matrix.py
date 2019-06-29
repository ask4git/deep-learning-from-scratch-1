
# -*- coding: utf-8 -*-

import numpy as np

if __name__ == '__main__':
    # vector
    a = np.array([1, 2, 3, 4])
    print(a)
    print(np.ndim(a))
    print(a.shape)
    print(a.shape[0])

    # matrix
    b = np.array([[1, 2], [3, 4], [5, 6]])
    print(b)
    print(np.ndim(b))
    print(b.shape)
    print(b.shape[0])

    # matrix multiplication
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    result = np.dot(a, b)   # np.dot(a, b) != np.dot(b, a)
    print(result)
    print(np.ndim(result))
    print(result.shape)

    # matrix multiplication 2
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([[1, 2], [3, 4], [5, 6]])
    print(a.shape)
    print(b.shape)
    result = np.dot(a, b)  # np.dot(a, b) != np.dot(b, a)
    print(result)
    print(np.ndim(result))
    print(result.shape)
