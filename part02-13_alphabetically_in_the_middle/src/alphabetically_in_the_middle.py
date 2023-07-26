# Write your solution here
first_letter = input("1st letter:")
second_letter = input("2nd letter:")
third_letter = input("3rd letter:")

letters = [first_letter, second_letter, third_letter]
letters.sort()

print(f"The letter in the middle is {letters[1]}")
