# Write your solution here
from collections import Counter


def most_common_character(string):
    return Counter(string).most_common()[0][0]


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
