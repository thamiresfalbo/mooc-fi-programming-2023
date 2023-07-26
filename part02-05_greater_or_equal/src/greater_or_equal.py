# Write your solution here
first_number = int(input("Please type in the first number:"))
second_number = int(input("Please type in the second number:"))

if first_number > second_number:
    print(f"The greater number was: {first_number}")
elif first_number < second_number:
    print(f"The greater number was: {second_number}")
else:
    print("The numbers are equal!")
