# Write your solution here
def new_person(name: str, age: int) -> tuple[str, int]:
    if len(name) == 0 or len(name.split()) < 2 or len(name) > 40:
        raise ValueError("The input was invalid.")
    elif age < 0 or age > 150:
        raise ValueError("The input was invalid.")

    my_tuple = (name, age)
    return my_tuple
