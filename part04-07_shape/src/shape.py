def line(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)


def triangle(size, character):
    for i in range(size + 1):
        line(i, character)


def shape(triangle_size, triangle_character, square_size, square_character):
    triangle(triangle_size, triangle_character)
    for i in range(square_size):
        line(triangle_size, square_character)


if __name__ == "__main__":
    shape(5, "x", 2, "o")
