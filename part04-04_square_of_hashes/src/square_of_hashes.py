# Copy here code of line function from previous exercise
# Copy here code of line function from previous exercise
def line(times, string):
    if string == "":
        string = "*"
    print(string[0] * times)


def square_of_hashes(size):
    # You should call function line here with proper parameters
    for i in range(size):
        line(size, "#")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
