# Write your solution here
def no_shouting(my_list):
    return list(filter(lambda item: item.isupper() == False, my_list))
