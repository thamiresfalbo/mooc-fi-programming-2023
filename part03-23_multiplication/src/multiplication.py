# Write your solution here
number = int(input("Please type in a number:"))
i = 1
j = 1
while j <= number:
    while i <= number:
        print(f"{j} x {i} = {j*i}")
        i += 1
    j += 1
    i = 1
