import random

class Board:

    def __init__(self):
        ""

    def _prepare(self):
        ""

    def board_string(self):
        ""

    def correct_guess(self, guess):
        """checks if the users guess is the number, and if it is returns True
        parameters:
            self: an instance of board
            guess: the players guessed number
            """
        
        if self.code == guess:
                return True
        return False
        

    def apply_guess(self):
        ""