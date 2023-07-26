# Write your solution here

items = int(input("How many items:"))
my_array = []

for i in range(items):
    my_number = int(input(f"Number {i}:"))
    my_array.append(my_number)

print(my_array)
