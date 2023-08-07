# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    persons = [person1, person2, person3]
    average = []

    for i in range(len(persons)):
        b = persons[i]["result1"] + persons[i]["result2"] + persons[i]["result3"] / 2
        average.append(b)

    average.sort()

    for i in range(len(persons)):
        c = persons[i]["result1"] + persons[i]["result2"] + persons[i]["result3"] / 2
        if average[0] == c:
            return persons[i]


if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))
