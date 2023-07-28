# Write your solution here
def filter_solutions():
    correct = []
    incorrect = []
    with open("solutions.csv") as solutions_file:
        for line in solutions_file:
            parts = line.split(";")
            if eval(parts[1]) == int(parts[2]):
                correct.append(line)
            else:
                incorrect.append(line)

    with open("correct.csv", "w") as correct_file:
        for i in correct:
            correct_file.write(i)

    with open("incorrect.csv", "w") as incorrect_file:
        for i in incorrect:
            incorrect_file.write(i)


if __name__ == "__main__":
    filter_solutions()
