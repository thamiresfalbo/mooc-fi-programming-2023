# Write your solution here
word = input("Word:")
right_side = int((28 - len(word)) / 2)
left_side = right_side + 1
print("*" * 30)

if len(word) % 2 == 0:
    print(f"*{' ' * right_side}{word}{' ' * right_side}*")
else:
    print(f"*{' ' * right_side}{word}{' ' * left_side}*")

print("*" * 30)
