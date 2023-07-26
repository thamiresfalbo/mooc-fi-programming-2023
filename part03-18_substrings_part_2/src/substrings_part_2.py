# Write your solution here
word = input("Please type in a string:")
count = 1

while count <= len(word):
    print(word[-count:])
    count += 1
