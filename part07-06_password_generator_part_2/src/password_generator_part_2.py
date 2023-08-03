# Write your solution here
from random import randint, choices, shuffle, choice
from string import ascii_lowercase, digits


def generate_strong_password(pass_len: int, want_numbers: bool, want_special: bool) -> str:
    special = choices("!?=+-()#", k=pass_len)
    password = list(choice(ascii_lowercase))
    numbers = choices(digits, k=pass_len)
    letters = choices(ascii_lowercase, k=pass_len)
    r = randint(1,2)

    if want_numbers:
        for i in range(r):
            password.append(numbers[i])

    if want_special:
        for i in range(r):
            password.append(special[i])

    while len(password) != pass_len:
        password.append(letters[randint(1, pass_len - 1)])

    # shuffle(password)
    return "".join(password)


if __name__ == "__main__":
    print(generate_strong_password(10, True, True))
    print(generate_strong_password(2, False, False))
