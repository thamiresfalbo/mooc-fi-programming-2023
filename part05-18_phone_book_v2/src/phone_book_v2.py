# Write your solution here
phone_book = {}

while True:
    user_command = int(input("command (1 search, 2 add, 3 quit):"))
    # Quits the phone book
    if user_command == 3:
        print("quitting...")
        break
    # Search for a phone number
    elif user_command == 1:
        search_name = input("name:")
        if search_name in phone_book:
            for numbers in phone_book[search_name]:
                print(numbers)
        else:
            print("no number")
    # Add new user, or add a new phone number to a existing user
    elif user_command == 2:
        new_name = input("name")
        new_phone_number = input("number:")
        if new_name in phone_book:
            phone_book.setdefault(new_name, []).extend([new_phone_number])
        else:
            # Better put the phone numbers in a list.
            phone_book[new_name] = [new_phone_number]
        print("ok!")
