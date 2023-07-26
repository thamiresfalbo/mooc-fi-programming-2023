# Write your solution here
def length_of_longest(my_list):
    return len(max(my_list, key=len))
