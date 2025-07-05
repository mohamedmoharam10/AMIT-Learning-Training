class Board:
    def  __init__(self):
        self.board = [str(i) for i in range(1, 10)]
    
    def display_board(self):
        """Prints the current state of the board."""
        for i in range(0, 9, 3):
            print('|'.join(self.board[i:i+3]))
            if  i < 5:
                print("- - -")

    def update_board(self, choice, symbol):
        """Updates the game board with a player's move."""
        # Check to see if the choice is existed
        if not (0 <= int(choice)-1 < len(self.board)):
            raise ValueError("Invalid input.")
        
        # Check to see if spot is already taken
        if self.board[choice-1].isdigit():
            self.board[choice-1] = symbol

            return True
            
    
    def reset_board(self):
        """Resets the game board back to its starting state."""
        self.__init__()
