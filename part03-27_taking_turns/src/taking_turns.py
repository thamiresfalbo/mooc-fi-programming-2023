# Write your solution here
number = int(input("Please type in a number: "))
index = 1
other_number = number
while index != other_number and other_number > index:
    print(index)
    print(other_number)
    index += 1
    other_number -= 1
if number % 2 != 0:
    print(index)
