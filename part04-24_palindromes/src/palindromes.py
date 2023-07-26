# Write your solution here
def palindromes(my_word):
    if my_word == my_word[::-1]:
        return True
    else:
        return False


while True:
    my_word = input("Please type in a palindrome:")
    if palindromes(my_word) == True:
        print(f"{my_word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
        continue


# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
