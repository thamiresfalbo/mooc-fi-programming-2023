# Write your solution here
hourly_wage = float(input("Hourly wage:"))
hours_worked = int(input("Hours worked:"))
weekday = input("Day of the week:")
daily_wages = hourly_wage * hours_worked

if weekday == "Sunday":
    daily_wages *= 2

print(f"Daily wages: {daily_wages} euros")
