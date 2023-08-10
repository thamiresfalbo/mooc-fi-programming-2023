# Write your solution here
phone_book = {}

while True:
    user_command = int(input("command (1 search, 2 add, 3 quit):"))
    if user_command == 3:
        print("quitting...")
        break
    elif user_command == 1:
        search_name = input("name:")
        if search_name in phone_book:
            print(phone_book[search_name])
        else:
            print("no number")
    elif user_command == 2:
        new_name = input("name")
        new_phone_number = input("number:")
        phone_book[new_name] = new_phone_number
        print("ok!")

