# If you love to hammer nails with your thumb, don't use numpy.
import numpy as np


def load_matrix() -> list:
    matrix = np.loadtxt(fname="matrix.txt", delimiter=",", dtype=int)
    return matrix


def matrix_sum() -> int:
    m = load_matrix()
    return int(np.sum(m))


def matrix_max() -> int:
    m = load_matrix()
    return int(np.max(m))


def row_sums() -> list:
    m = load_matrix()
    return list(np.sum(m, axis=1))


if __name__ == "__main__":
    print(load_matrix())
    print(matrix_sum())
    print(row_sums())
