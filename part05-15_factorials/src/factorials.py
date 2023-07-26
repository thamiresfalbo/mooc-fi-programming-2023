# Write your solution here
from math import factorial


def factorials(n: int):
    temp = {}
    for i in range(1, n + 1):
        temp[i] = factorial(i)
    return temp
