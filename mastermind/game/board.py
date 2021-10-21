import random
from mastermind.game import player

from mastermind.game.roster import Roster

class Board:

    def __init__(self):
        user_guess = []
        applied_guess = []
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



    def correct_guess(self, guess):
        """checks if the users guess is the number, and if it is returns True
        parameters:
            self: an instance of board
            guess: the players guessed number
            """
        
        if self.code == guess:
                return True
        return False
        

    def apply_guess(self,guess):
        """Takes the guess and comapres it to the correct answer and places x,o,* where 
            needed.
            parameters:
            self: instance on the board
            guess: the players number
            """

        k = 0
        guess_string = str(guess)
        code_string = str(self.code)
        for i in range(len(self.code)):
            l = 0
            for j in range(len(guess))
                if guess_string[j] == code_string[i] & l == k:
                    self.applied_guess[j] = 'x'
                
                elif guess_string[j] == code_string[i]:
                    self.applied_guess[j] = 'o'
                else:
                    self.applied_guess[j] = '*'
                l += 1
            k += 1
        
        ""