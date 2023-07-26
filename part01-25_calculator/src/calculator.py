# Write your solution here
first_number = int(input("Number 1: "))
second_number = int(input("Number 2: "))
operation = input("Operation:")

if operation == "add":
    print(f"{first_number} + {second_number} = {first_number + second_number}")
elif operation == "multiply":
    print(f"{first_number} * {second_number} = {first_number * second_number}")
elif operation == "subtract":
    print(f"{first_number} - {second_number} = {first_number - second_number}")
