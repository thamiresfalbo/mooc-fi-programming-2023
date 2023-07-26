# Write your solution here
def histogram(string):
    grouped = {}
    for i in string.strip():
        if i not in grouped:
            grouped[i] = 1
        else:
            grouped[i] += 1

    for key, value in grouped.items():
        print(f"{key} {value * '*'}")

    print()


if __name__ == "__main__":
    histogram("abba")
    histogram("statistically")
    histogram("musculus sternocleidomastoideus")
