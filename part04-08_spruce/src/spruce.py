# Write your solution here
# You can test your function by calling it within the following block


def line(size):
    print("*" * size)


def space(size):
    print(" " * size, end="")


def triangle(size):
    for i in range(size + 1):
        space(size - i)
        line((2 * i) - 1)


def spruce(size):
    print("a spruce!", end="")
    triangle(size)
    space(size - 1)
    line(1)


if __name__ == "__main__":
    spruce(5)
