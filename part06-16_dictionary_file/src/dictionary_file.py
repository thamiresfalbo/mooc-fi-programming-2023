# Write your solution here
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    user_input = int(input("Function:"))

    # Add
    if user_input == 1:
        finnish = input("The word in Finnish:")
        english = input("The word in English:")

        with open("dictionary.txt", "a") as f:
            f.write(f"{finnish};{english}\n")

        print("Dictionary entry added")

    # Search
    if user_input == 2:
        searched_term = input("Search term:")
        with open("dictionary.txt", "r") as f:
            for line in f:
                parts = line.split(";")
                if searched_term in parts[0] or searched_term in parts[1]:
                    print(f"{parts[0]} - {parts[1]}")

    # Quit
    if user_input == 3:
        print("Bye!")
        break
