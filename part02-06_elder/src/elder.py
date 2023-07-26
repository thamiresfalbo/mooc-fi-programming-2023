# Write your solution here
print("Person 1:")
first_person_name = input("Name:")
first_person_age = int(input("Age:"))

print("Person 2:")
second_person_name = input("Name: ")
second_person_age = int(input("Age: "))

if first_person_age > second_person_age:
    print(f"The elder is {first_person_name}")
elif first_person_age < second_person_age:
    print(f"The elder is {second_person_name}")
else:
    print(f"{first_person_name} and {second_person_name} are the same age")
