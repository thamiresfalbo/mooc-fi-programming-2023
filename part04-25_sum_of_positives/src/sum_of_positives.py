# Write your solution here
def sum_of_positives(my_list):
    temp_list = []
    for i in my_list:
        if i > 0:
            temp_list.append(i)
    return sum(temp_list)
