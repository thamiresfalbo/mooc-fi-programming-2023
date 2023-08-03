# Write your solution here
import random
import string


def generate_password(lenght: int) -> str:
    letters = string.ascii_lowercase
    z = random.choices(letters, k=lenght)
    return "".join(z)


if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))
