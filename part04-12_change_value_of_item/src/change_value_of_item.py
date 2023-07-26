# Write your solution here
nums = [*range(1, 6)]

while True:
    my_index = int(input("Index:"))
    if my_index == -1:
        break

    new_value = int(input("New Value:"))
    nums[my_index] = new_value
    print(nums)
