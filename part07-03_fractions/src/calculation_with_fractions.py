# Write your solution here
from fractions import Fraction


def fractionate(amount: int):
    fractions = []
    for number in range(amount):
        fractions.append(Fraction(1, amount))
    return fractions
