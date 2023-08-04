# Write your solution here
from datetime import datetime, timedelta
from copy import copy

filename = input("Filename:")
starting_date = input("Starting date:")
how_many_days = int(input("How many days:"))

starting_date = datetime.strptime(starting_date, "%d.%m.%Y")
end_date = copy(starting_date)

lines = []
minutes = []

print("Please type in screen time in minutes on each day (TV computer mobile):")
for i in range(how_many_days):
    formatted_end_date = datetime.strftime(end_date, "%d.%m.%Y")
    line = input(f"Screen time {formatted_end_date}:")
    parts = line.split(" ")
    lines.append(f"{formatted_end_date}: {parts[0]}/{parts[1]}/{parts[2]}")
    for j in range(len(parts)):
        minutes.append(int(parts[j]))
    end_date += timedelta(days=1)


with open(filename, "w") as file:
    formatted_starting_date = datetime.strftime(starting_date, "%d.%m.%Y")
    minutes_sum = sum(minutes)
    minutes_average = minutes_sum / how_many_days

    file.write(f"Time period: {formatted_starting_date}-{formatted_end_date}\n")
    file.write(f"Total minutes: {minutes_sum}\n")
    file.write(f"Average minutes: {minutes_average:.1f}\n")

    for l in range(how_many_days):
        file.write(lines[l] + "\n")
    print(f"Data stored in {filename}")
