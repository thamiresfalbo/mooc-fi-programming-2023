# Write your solution here
def longest_series_of_neighbours(my_list: list):
    a = 1
    b = 1
    for item in range(1, len(my_list)):
        if abs(my_list[item - 1] - my_list[item]) == 1:
            b += 1
        else:
            b = 1
        a = max(a, b)
    return a


if __name__ == "__main__":
    example = [1, 2, 5, 4, 3, 4]
    # should give [5, 4, 3, 4]
    print(longest_series_of_neighbours(example))
