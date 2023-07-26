# Write your solution here
import math

while True:
    number = int(input("Please type in a number:"))
    if number <= 0:
        print("Thanks and bye!")
        break
    print(f"The factorial of the number {number} is {math.factorial(number)}")
