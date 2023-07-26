# Write your solution here
# You can test your function by calling it within the following block
def same_chars(word, first_number, second_number):
    if second_number < len(word) and first_number < len(word):
        return word[first_number] == word[second_number]
    else:
        return False


if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
