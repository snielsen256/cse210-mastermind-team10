import random

class Board:

    def __init__(self):

        
        ""

        """The class constructor.
        
        Args:
            self (Board): an instance of Board
        """
        self.user_guess = []
        self.applied_guess = []
        self.code = 0
        self._prepare()

    def _prepare(self):
        """Sets up the initial board to be used in the game
        
        Args:
            self (Board): an instance of Board
        """
        self.code = random.randint(1000,9999)
        self.user_guess.append("----")
        self.user_guess.append("----")
        self.applied_guess.append("****")
        self.applied_guess.append("****")
    def board_string(self, players):
        """Turns the board into a string to be printed 

        Args:
            self (Board): an instance of Board
        """
        if len(self.user_guess) == 1:
            board = "\n-------------------\n"
            board += f"Player {players[0]}: {self.user_guess[0]}, {self.applied_guess[0]}\n"
            board += f"Player {players[1]}: {self.user_guess[0]}, {self.applied_guess[0]}\n"
            board += "-------------------\n"

        board = "\n-------------------\n"
        board += f"Player {players[0]}: {self.user_guess[0]}, {self.applied_guess[-1]}\n"
        board += f"Player {players[1]}: {self.user_guess[1]}, {self.applied_guess[-2]}\n"
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
        

    def apply_guess(self,guess, current):
        """Takes the guess and comapres it to the correct answer and places x,o,* where 
            needed.
            parameters:
            self: instance on the board
            guess: the players number
            """

        k = 0
        guess_string = str(guess)
        code_string = str(self.code)
        revealed = ["*", "*", "*", "*"]

        for i in range(len(code_string)):
            l = 0
            for j in range(len(guess_string)):
                if guess_string[j] == code_string[i] and l == k:
                    revealed[l] = 'x'
                
                elif guess_string[j] == code_string[i]:
                    revealed[l] = 'o'
                
                l += 1
            k += 1
        
        m = ""
        for i in revealed:
            m += i
        self.applied_guess[current] = m
        self.user_guess[current] = guess
        ""