class Turn:
    """A maneuver in the game. The responsibility of Turn is to keep track of the guess.
    
    Stereotype: 
        Information Holder

    Attributes:
        _guess (integer): The player guess.
        
    """
    def __init__(self, guess):
        """The class constructor.
        
        Args:
            self (Turn): an instance of Turn.
        """
        self._guess = guess

    def get_guess(self):
        """Returns the guess.

        Args:
            self (Turn): an instance of Turn.
        """
        return self._guess