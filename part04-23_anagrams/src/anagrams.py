# Write your solution here
def anagrams(first_word, second_word):
    if sorted(first_word) == sorted(second_word):
        return True
    else:
        return False
