# write your solution here
def read_fruits():
    fruits = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = str(parts[0])
            price = float(parts[1])
            fruits[name] = price
    return fruits
