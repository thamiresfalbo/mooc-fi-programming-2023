# Write your solution here
phrase = ""
my_word = ""
while True:
    previous_word = my_word
    my_word = input("Please type in a word:")
    if my_word == "end" or my_word == previous_word:
        break
    phrase += my_word + " "

print(phrase)
