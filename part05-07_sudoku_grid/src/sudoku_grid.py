# Write your solution here
import numpy as np

# Please write a function named sudoku_grid_correct(sudoku: list), which takes a two-dimensional array representing a
# sudoku grid as its argument. The function should use the functions from the three previous exercises to determine
# whether the complete sudoku grid is filled in correctly. Copy the functions from the exercises above into your Python
# code file for this exercise.

# The function should check each of the nine rows, columns and 3 by 3 blocks in the grid. If all contain each of the
# numbers 1 to 9 at most once, the function returns True. If a single one is filled in incorrectly, the function returns
# False.

# The image of a sudoku grid above these exercises has the nine blocks within the grid indicated with thicker borders.
# These are the blocks the function should check, and they begin at the indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3),
# (3, 6), (6, 0), (6, 3) and (6, 6).


def row_correct(sudoku: list, row_no: int):
    for i in sudoku[row_no]:
        if i == 0:
            pass
        elif sudoku[row_no].count(i) > 1:
            return False
    return True


def column_correct(sudoku: list, column_no: int):
    my_col = [row[column_no] for row in sudoku]
    for i in my_col:
        if i == 0:
            pass
        elif my_col.count(i) > 1:
            return False
    return True


def block_correct(sudoku: list, row_no: int, column_no: int):
    my_block = np.array(sudoku)[row_no : row_no + 3, column_no : column_no + 3]
    for i in range(1, 10):
        if np.count_nonzero(my_block == i) > 1:
            return False
    return True


def sudoku_grid_correct(sudoku: list):
    for i in range(len(sudoku)):
        if row_correct(sudoku, i) == False:
            return False

    for j in range(len(sudoku)):
        if column_correct(sudoku, j) == False:
            return False

    for k in range(0, 7, 3):
        for l in range(0, 7, 3):
            if block_correct(sudoku, k, l) == False:
                return False
    return True


if __name__ == "__main__":
    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1],
    ]

    print(sudoku_grid_correct(sudoku2))
