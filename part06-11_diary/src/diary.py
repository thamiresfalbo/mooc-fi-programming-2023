# Write your solution here
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    user_input = int(input("Function:"))
    if user_input == 1:
        user_entry = input("Diary entry:")
        with open("diary.txt", "a") as f:
            f.write(f"{user_entry}\n")
        print("Diary saved")
    elif user_input == 2:
        with open("diary.txt") as f:
            for line in f:
                print(line)
    elif user_input == 0:
        print("Bye now!")
        break
