# Write your solution here


def all_the_longest(my_list):
    temp_array = []
    temp_array.append(max(my_list, key=len))
    for i in my_list:
        if i == temp_array[0]:
            pass
        elif len(i) == len(temp_array[0]):
            temp_array.append(i)
    return temp_array
