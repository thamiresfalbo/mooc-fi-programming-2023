# Write your solution here
def filter_incorrect():
    counter = 0
    with open("lottery_numbers.csv") as lottery_numbers_csv:
        for line in lottery_numbers_csv:
            parts = line.split(";")
            week = parts[0].split()
            numbers = set(parts[1].split(","))

            try:
                if not isinstance(int(week[1]), int):
                    raise ValueError

                check_numbers(numbers)

                if counter == 0:
                    with open("correct_numbers.csv", "w") as correct_csv:
                        correct_csv.write(line)
                        counter += 1
                else:
                    with open("correct_numbers.csv", "a") as correct_csv:
                        correct_csv.write(line)

            except:
                pass


def check_numbers(numbers_list):
    if len(numbers_list) == 7:
        pass
    else:
        raise ValueError

    for number in numbers_list:
        if isinstance(int(number), int):
            pass

        if int(number) > 40 or int(number) < 1:
            raise ValueError


if __name__ == "__main__":
    filter_incorrect()
