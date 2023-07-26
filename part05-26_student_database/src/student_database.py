# Write your solution here
import numpy as np


def add_student(students: dict, student_name: str):
    students.setdefault(student_name, [])


def print_student(students: dict, student_name: str):
    if student_name in students.keys():
        student_courses = students[student_name]
        notes = []
        print(f"{student_name}:")
        if student_courses == []:
            print(f" no completed courses")
        else:
            print(f" {len(student_courses)} completed courses:")
            for i in range(len(student_courses)):
                print(f"  {student_courses[i][0]} {student_courses[i][1]}")
                notes.append(student_courses[i][1])
            print(f" average grade {np.average(notes):.1f}")
    else:
        print(f"{student_name}: no such person in the database")


def add_course(students: dict, student_name: str, course: tuple):
    # for i in students[student_name]:
    #     if course[0] == i[0] and course[1] > i[1]:
    #         students[student_name].remove(i)

    # if course not in students[student_name] and course[1] != 0:
    #     students[student_name].append(course)
    pass


def summary(database: dict):
    pass


if __name__ == "__main__":
    # # Part I
    # students = {}
    # add_student(students, "Peter")
    # add_student(students, "Eliza")
    # print_student(students, "Peter")
    # print_student(students, "Eliza")
    # print_student(students, "Jack")

    # # Part II
    # students = {}
    # add_student(students, "Peter")
    # add_course(students, "Peter", ("Introduction to Programming", 3))
    # add_course(students, "Peter", ("Advanced Course in Programming", 2))
    # print_student(students, "Peter")

    # # Part III
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    print_student(students, "Peter")

    # Part IV
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    # summary(students)
