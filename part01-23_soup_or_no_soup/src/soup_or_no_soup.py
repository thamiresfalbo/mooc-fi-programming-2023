# Write your solution here
name = input("Please tell me your name:")
price = 5.9
if name == "Jerry":
    print("Next please!")
else:
    portions = int(input("How many portions of soup?"))
    print(f"The total cost is {price * portions}")
    print("Next please!")
