# Write your solution here
import urllib.request
import json
import math
from os.path import exists


def retrieve_all():
    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    my_request = urllib.request.urlopen(address)

    data = my_request.read()
    JSON_obj = json.loads(data)
    courses = []

    for course in JSON_obj:
        if course["enabled"]:
            temp = (
                course["fullName"],
                course["name"],
                course["year"],
                sum(course["exercises"]),
            )
            courses.append(temp)

    return courses


def retrieve_course(course_name: str) -> dict[str, int]:
    course = {
        "weeks": 0,
        "students": 0,
        "hours": 0,
        "hours_average": 0,
        "exercises": 0,
        "exercises_average": 0,
    }

    adress = (
        f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    )
    request = urllib.request.urlopen(adress)
    data = request.read()
    JSON_obj = json.loads(data)

    first_key = next(iter(JSON_obj))
    course["students"] += JSON_obj[first_key]["students"]
    for k in JSON_obj.keys():
        course["weeks"] += 1
        course["hours"] += JSON_obj[k]["hour_total"]
        course["exercises"] += JSON_obj[k]["exercise_total"]

    course["exercises_average"] = math.floor(course["exercises"] / course["students"])
    course["hours_average"] = math.floor(course["hours"] / course["students"])

    return course


if __name__ == "__main__":
    # retrieve_all()
    retrieve_course("docker2019")
