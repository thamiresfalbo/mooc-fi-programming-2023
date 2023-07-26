# Write your solution here
def chessboard(number):
    values = ["0", "1"]
    for i in range(number):
        for j in range(number):
            z = values[(i + j + 1) % 2]
            print(z, end="")
        print()


# Testing the function
if __name__ == "__main__":
    chessboard(3)
