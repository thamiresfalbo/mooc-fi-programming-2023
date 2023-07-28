# Write your solution here
import fnmatch


def find_words(search_term: str):
    wordlist = []
    with open("words.txt") as f:
        for line in f:
            wordlist.append(line.strip())

    search_term = search_term.replace(".", "?")
    filtered = fnmatch.filter(wordlist, search_term)

    return filtered


if __name__ == "__main__":
    print(find_words("*vokes"))
