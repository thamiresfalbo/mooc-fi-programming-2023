# Work smarter, not harder!
from itertools import cycle, islice


def squared(phrase, number):
    letters = cycle(phrase)  # lazy iterator -> abcabcabcabc....
    for i in range(number):
        print("".join(islice(letters, number)))


# Testing the function
if __name__ == "__main__":
    squared("boatmcboatface", 5)
