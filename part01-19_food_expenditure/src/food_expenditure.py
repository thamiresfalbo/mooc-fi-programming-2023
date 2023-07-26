# Write your solution here
times_a_week = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
spend = float(input("How much money do you spend on groceries in a week?"))

total = (float(times_a_week) * price) + spend

print(f"Average food expenditure:")
print(f"Daily: {total/7} euros")
print(f"Weekly: {total} euros")
