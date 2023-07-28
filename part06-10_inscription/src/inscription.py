# Write your solution here
my_name = input("Whom should I sign this to:")
my_file = input("Where shall I save it:")
with open(my_file, "w") as f:
    f.write(
        f"Hi {my_name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team"
    )
