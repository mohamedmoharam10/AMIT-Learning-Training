class Player:
    def  __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        name = input('Enter your name: ')
        self.name = name.capitalize()

    def set_symbol(self):
        symbol = input(f"{self.name}, please enter the symbol you want to use (either 'X' or 'O'): ")
        while True:
            if len(symbol) != 1 or symbol.upper() not in ['X', 'O']:
                print("Invalid Symbol! Please enter either 'X' or 'O'.")
                symbol = input("Please enter again: ")
            else:
                self.symbol = symbol.upper()
                break
        return f"\nWelcome {self.name}! You will be playing as '{self.symbol}'."