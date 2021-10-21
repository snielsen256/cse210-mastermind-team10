import random

class Board:

    def __init__(self):
        ""
        self.code = 0

    def _prepare(self):
        ""
        self.code = random.randint(1000,9999)

    def board_string(self, player1, player2):
        ""
        if len(self.user_guess) == 1:
            board = "\n-------------------\n"
            board += f"Player {player1}: {self.user_guess[0]}, {self.applied_guess[0]}\n"
            board += f"Player {player2}: {self.user_guess[0]}, {self.applied_guess[0]}\n"
            board += "-------------------\n"

        board = "\n-------------------\n"
        board += f"Player {player1}: {self.user_guess[-1]}, {self.applied_guess[-1]}\n"
        board += f"Player {player2}: {self.user_guess[-2]}, {self.applied_guess[-2]}\n"
        board += "-------------------\n"

        return board



    def check_guess(self):
        ""

    def apply_guess(self):
        ""