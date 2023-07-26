# Write your solution here
def oldest_person(people: list):
    oldest = []
    for i in range(len(people)):
        oldest.append(people[i][1])

    for j in range(len(people)):
        if people[j][1] == sorted(oldest)[0]:
            return people[j][0]


if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))
