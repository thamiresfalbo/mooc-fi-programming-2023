# Write your solution here
from datetime import datetime

millenium = datetime(1999, 12, 31)
day = int(input("Day:"))
month = int(input("Month:"))
year = int(input("Year:"))

user_birth = datetime(year, month, day)
subtracted = millenium - user_birth

if subtracted.days > 0:
    print(f"You were {subtracted.days} days old on the eve of the new millennium.")
else:
    print(f"You weren't born yet on the eve of the new millennium.")
