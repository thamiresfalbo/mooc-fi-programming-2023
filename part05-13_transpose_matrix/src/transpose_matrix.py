# Write your solution here
import numpy as np


def transpose(matrix: list) -> None:
    matrix[:] = [list(x) for x in zip(*matrix)]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix)
    transpose(matrix)
    print(matrix)
