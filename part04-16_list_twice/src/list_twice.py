# Write your solution here
arr = []

while True:
    number = int(input("New number:"))
    if number == 0:
        print("Bye!")
        break
    arr.append(number)
    print(f"The list now: {arr}")
    print(f"The list in order: {sorted(arr)}")
