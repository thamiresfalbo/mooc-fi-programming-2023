# write your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points:")
    course_info = input("Course information:")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"
    course_info = "course1.txt"

students = {}
exercises = {}
exams = {}
course = {}

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

with open(course_info) as course_file:
    for line in course_file:
        parts = line.split(":")
        course[parts[0]] = parts[1].strip()


def get_key(val):
    for key, value in students.items():
        if val == value:
            return key


with open("results.txt", "w") as f:
    with open("results.csv", "w") as z:
        name = "name"
        exec_nbr = "exec_nbr"
        exec_pts = "exec_pts."
        exm_pts = "exm_pts."
        tot_pts = "tot_pts."
        grade = "grade"

        course_name = f"{course['name']}, {course['study credits']} credits"
        f.write(course_name + "\n")
        f.write("=" * len(course_name) + "\n")
        f.write(f"{name:30}{exec_nbr:10}{exec_pts:10}{exm_pts:10}{tot_pts:10}{grade}\n")

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

            f.write(
                f"{name:30}{sum(exercises[id]):<10}{exercise_points:<10}{sum(exam_points):<10}{my_points:<10}{grade}\n"
            )
            z.write(f"{get_key(name)};{name};{grade}\n")


print("Results written to files results.txt and results.csv")
