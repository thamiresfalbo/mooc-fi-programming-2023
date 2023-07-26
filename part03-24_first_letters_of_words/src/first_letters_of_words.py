# Write your solution here
sentence = input("Please type in a sentence:")
array = sentence.split(" ")

for i in range(len(array)):
    print(array[i][0])
