# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if self.count_numbers() == 0:
            return 0
        else:
            return self.get_sum() / self.count_numbers()


all_numbers = NumberStats()
odd_numbers = NumberStats()
even_numbers = NumberStats()
while True:
    num = int(input("Please type in integer numbers:"))
    if num == -1:
        break

    if num % 2 == 0:
        even_numbers.add_number(num)
    else:
        odd_numbers.add_number(num)

    all_numbers.add_number(num)

print(f"Sum of numbers: {all_numbers.get_sum()}")
print(f"Mean of numbers: {all_numbers.average()}")
print(f"Sum of even numbers: {even_numbers.get_sum()}")
print(f"Sum of odd numbers: {odd_numbers.get_sum()}")
