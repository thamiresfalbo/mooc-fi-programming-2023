# WRITE YOUR SOLUTION HERE:
from collections import Counter


class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        c = Counter(my_list).most_common()
        return c[0][0]

    @classmethod
    def doubles(cls, my_list: list):
        counter = 0
        c = Counter(my_list).most_common()
        for i in c:
            if i[1] >= 2:
                counter += 1
        return counter


if __name__ == "__main__":
    # numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    # print(ListHelper.greatest_frequency(numbers))
    # print(ListHelper.doubles(numbers))
    num = [3, 2, 3, 2, 2, 3, 1, 2, 4, 5, 5, 6]
    print(ListHelper.doubles(num))
