# Write your solution here
# You can test your function by calling it within the following block


def greatest_number(first_number, second_number, third_number):
    my_array = [first_number, second_number, third_number]
    my_array.sort()
    return my_array[2]


if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)
