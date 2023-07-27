# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

students = {}
exercises = {}

with open(student_info) as student_file:
    for line in student_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1].strip()} {parts[2].strip()}"

with open(exercise_data) as exercise_file:
    for line in exercise_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exercises[parts[0]] = list(map(int, parts[1:]))

for id, name in students.items():
    if id in exercises:
        exercise_points = exercises[id]

    print(f"{name} {sum(exercise_points)}")
