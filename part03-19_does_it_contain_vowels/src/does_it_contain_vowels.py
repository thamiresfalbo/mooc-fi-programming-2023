# Write your solution here
word = input("Please type in a string:")
vowels = "aeo"
index = 0

while index < len(vowels):
    substring = vowels[index]
    if substring in word:
        print(f"{substring} found")
    else:
        print(f"{substring} not found")
    index += 1
