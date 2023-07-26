# Write your solution here
def column_correct(sudoku: list, column_no: int):
    my_col = [row[column_no] for row in sudoku]
    for i in my_col:
        if i == 0:
            pass
        elif my_col.count(i) > 1:
            return False
    return True
