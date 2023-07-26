# Write your solution here
def remove_smallest(my_list: list) -> None:
    my_list.remove(min(my_list))


if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    # Should be [2, 4, 6, 3, 5]
    remove_smallest(numbers)
    print(numbers)
