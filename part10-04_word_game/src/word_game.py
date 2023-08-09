# Write your solution here
import random


class WordGame:
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass  # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            return 0


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels = "aeiou"
        player1_vowels = list(filter(lambda x: x in vowels, player1_word))
        player2_vowels = list(filter(lambda x: x in vowels, player2_word))

        if len(player1_vowels) > len(player2_vowels):
            return 1
        elif len(player1_vowels) < len(player2_vowels):
            return 2
        else:
            return 0


class RockPaperScissors(WordGame):
    """
    The rules of the game are as follows:

    rock beats scissors (the rock can break the scissors but the scissors can't cut the rock)
    paper beats rock (the paper can cover the rock)
    scissors beats paper (the scissors can cut the paper)

    """

    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        s = {"rock": 0, "paper": 1, "scissors": 2}
        # Check if input is valid
        if player1_word not in s.keys() and player2_word not in s.keys():
            return 0
        elif player1_word not in s.keys():
            return 2
        elif player2_word not in s.keys():
            return 1

        # ½   R   P   S
        # R   0   2   1
        # P   1   0   2
        # S   2   1   0

        k = [[0, 2, 1], [1, 0, 2], [2, 1, 0]]
        p1 = s[player1_word]
        p2 = s[player2_word]
        m = k[p1][p2]
        return m


if __name__ == "__main__":
    p = MostVowels(3)
    p.play()
