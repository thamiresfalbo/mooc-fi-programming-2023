# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points:")

students = {}
exercises = {}
exams = {}

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

with open(exam_data) as exam_file:
    for line in exam_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exams[parts[0]] = list(map(int, parts[1:]))

for id, name in students.items():
    if id in exams:
        exam_points = exams[id]
    exercise_points = int(sum(exercises[id]) / 40 * 10)
    my_points = sum(exam_points) + exercise_points
    grade = 0
    if my_points >= 28:
        grade = 5
    elif my_points >= 24:
        grade = 4
    elif my_points >= 21:
        grade = 3
    elif my_points >= 18:
        grade = 2
    elif my_points >= 15:
        grade = 1

    print(f"{name} {grade}")
