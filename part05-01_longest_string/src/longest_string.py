# Write your solution here
def longest(my_list: list):
    return sorted(my_list, key=len)[-1]


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
