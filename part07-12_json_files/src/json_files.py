# Write your solution here
import json


def print_persons(filename: str):
    with open(filename) as f:
        data = f.read()

    data_json = json.loads(data)
    for i in range(len(data_json)):
        name = data_json[i]["name"]
        age = data_json[i]["age"]
        hobbies = ", ".join(data_json[i]["hobbies"])
        print(f"{name} {age} years ({hobbies})")


if __name__ == "__main__":
    print_persons("file3.json")
