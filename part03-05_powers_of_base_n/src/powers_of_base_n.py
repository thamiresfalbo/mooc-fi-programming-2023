# Write your solution here
my_limit = int(input("Upper limit:"))
my_base = int(input("Base:"))
my_number = 1
while my_number > 0 and my_number <= my_limit:
    print(my_number)
    my_number *= my_base
