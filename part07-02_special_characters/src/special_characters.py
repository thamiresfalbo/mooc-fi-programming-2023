# Write your solution here
import string


def separate_characters(my_string: str):
    a, b, c = "", "", ""
    for i in my_string:
        if i in string.ascii_letters:
            a += i
        elif i in string.punctuation:
            b += i
        elif i not in string.ascii_letters and i not in string.punctuation:
            c += i
    return (a, b, c)


if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
