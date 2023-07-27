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

name = "name"
exec_nbr = "exec_nbr"
exec_pts = "exec_pts."
exm_pts = "exm_pts."
tot_pts = "tot_pts."
grade = "grade"

print(f"{name:30}{exec_nbr:10}{exec_pts:10}{exm_pts:10}{tot_pts:10}{grade}")

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

    print(
        f"{name:30}{sum(exercises[id]):<10}{exercise_points:<10}{sum(exam_points):<10}{my_points:<10}{grade}"
    )
