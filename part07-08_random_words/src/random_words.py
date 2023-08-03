import re
import random


def words(amount: int, search_term: str) -> list:
    words = []
    try:
        with open("words.txt") as f:
            for line in f:
                if re.match(search_term, line):
                    words.append(line.strip())

    except:
        pass

    return random.sample(words, amount)


if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)
