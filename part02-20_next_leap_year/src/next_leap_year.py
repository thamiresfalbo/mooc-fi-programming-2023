# Write your solution here
my_year = int(input("Please type in a year:"))

for i in range(my_year + 1, 3000):
    if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
        print(f"The next leap year after {my_year} is {i}")
        break
