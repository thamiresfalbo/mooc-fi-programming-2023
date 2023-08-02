# Write your solution here
def read_input(phrase: str, first_number: int, second_number: int):
    while True:
        try:
            number = int(input(phrase))
            if number > first_number and number < second_number:
                return number
        except ValueError:
            pass
        print(f"You must type in an integer between {first_number} and {second_number}")


if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
