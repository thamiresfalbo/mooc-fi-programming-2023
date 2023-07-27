# write your solution here


def largest():
    with open("numbers.txt") as file:
        number = 0
        for line in file:
            if int(line) > number:
                number = int(line)
    return number
