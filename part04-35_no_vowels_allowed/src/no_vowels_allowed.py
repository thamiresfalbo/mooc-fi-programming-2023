# Write your solution here
import re


def no_vowels(my_string):
    return re.sub(r"[aeiou]", "", my_string)
