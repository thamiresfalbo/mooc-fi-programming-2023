# Write your solution here
arr = []

while True:
    print(f"The list is now {arr}")
    user_command = input("a(d)d, (r)emove or e(x)it:")
    if user_command == "x":
        print("Bye!")
        break
    elif user_command == "d":
        if len(arr) == 0:
            arr.append(1)
        else:
            arr.append(arr[-1] + 1)
    elif user_command == "r":
        arr.pop(-1)
