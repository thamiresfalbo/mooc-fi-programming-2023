# Write your solution here


def distinct_numbers(my_list):
    temp_list = []
    for i in my_list:
        if i in temp_list:
            pass
        else:
            temp_list.append(i)
    return sorted(temp_list)
