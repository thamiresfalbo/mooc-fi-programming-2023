from random import choice


# Gambling was never my vice...
def roll(die: str) -> str:
    dies = {"A": (3, 3, 3, 3, 3, 6), "B": (2, 2, 2, 5, 5, 5), "C": (1, 4, 4, 4, 4, 4)}

    return choice(dies[die])


def play(die1: str, die2: str, times: int) -> tuple[int, int, int]:
    dies = {"A": (3, 3, 3, 3, 3, 6), "B": (2, 2, 2, 5, 5, 5), "C": (1, 4, 4, 4, 4, 4)}
    die1_win = 0
    die2_win = 0
    ties = 0

    for _ in range(times):
        cast_die1 = choice(dies[die1])
        cast_die2 = choice(dies[die2])
        if cast_die1 > cast_die2:
            die1_win += 1
        elif cast_die1 < cast_die2:
            die2_win += 1
        else:
            ties += 1

    return (die1_win, die2_win, ties)


if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")

    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)
