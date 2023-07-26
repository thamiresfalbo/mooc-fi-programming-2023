# Write your solution here
secret_password = "sekred"


password = input("Password:")
repeat_password = input("Repeat password:")
while password != repeat_password:
    print("They do not match!")
    repeat_password = input("Repeat password:")


print("User account created!")
