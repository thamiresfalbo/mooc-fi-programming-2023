# Write your solution here
word = input("Please type in a word:")
character = input("Please type in a character:")

if word.find(character) + 3 < len(word):
    print(word[word.find(character) : word.find(character) + 3])
