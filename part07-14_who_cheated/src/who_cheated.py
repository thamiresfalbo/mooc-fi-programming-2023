# Write your solution here
import csv
from datetime import datetime, timedelta


def cheaters() -> list:
    students = {}
    cheaters = []

    with open("start_times.csv") as start_file:
        a = csv.reader(start_file, delimiter=";")
        for row in a:
            name = row[0]
            start_time = datetime.strptime(row[1], "%H:%M")
            students[name] = {"start_time": start_time, "submissions": []}

    with open("submissions.csv") as submissions_file:
        b = csv.reader(submissions_file, delimiter=";")
        for row in b:
            name = row[0]
            task = row[1]
            points = row[2]
            end_time = datetime.strptime(row[3], "%H:%M")
            g = {"task": task, "points": points, "end_time": end_time}
            students[name]["submissions"].append(g)

    for key, _ in students.items():
        student_submission = students[key]["submissions"]
        student_start_time = students[key]["start_time"]
        for submission in student_submission:
            if submission["end_time"] > (student_start_time + timedelta(hours=3)):
                cheaters.append(key)
                break

    return cheaters


if __name__ == "__main__":
    cheaters()
