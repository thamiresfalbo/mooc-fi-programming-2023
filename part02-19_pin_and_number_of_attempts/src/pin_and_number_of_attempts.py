# Write your solution here
attempt = 0

while True:
    my_pin = int(input("PIN:"))
    if my_pin == 4321:
        attempt += 1
        break
    print("Wrong")
    attempt += 1

if attempt == 1 or attempt == 0:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempt} attempts")
