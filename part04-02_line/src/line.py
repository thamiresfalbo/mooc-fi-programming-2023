# Write your solution here
# You can test your function by calling it within the following block
def line(times, string):
    if string == "":
        string = "*"
    print(string[0] * times)


if __name__ == "__main__":
    line(5, "xxx")
