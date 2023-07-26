# Write your solution here
count = 0
sum = 0
negative_numbers = 0
positive_numbers = 0
print("Please type in integer numbers. Type in 0 to finish.")

while True:
    my_number = int(input("Number: "))
    if my_number == 0:
        break
    count += 1
    sum += my_number
    if my_number < 0:
        negative_numbers += 1
    else:
        positive_numbers += 1


print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {float(sum/count)}")
print(f"Positive numbers {positive_numbers}")
print(f"Negative numbers {negative_numbers}")
