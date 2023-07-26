# Write your solution here


def row_correct(sudoku: list, row_no: int):
    for i in sudoku[row_no]:
        if i == 0:
            pass
        elif sudoku[row_no].count(i) > 1:
            return False
    return True
