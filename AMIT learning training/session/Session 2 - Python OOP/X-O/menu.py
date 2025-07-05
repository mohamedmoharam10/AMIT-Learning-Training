class Menu:
    def display_main_menu(self):
        print("\nWelcome to the X-O game")
        print("Please choose an option from the following menu: ")
        print("1. Start a new game.")
        print("2. Quit the game.")

        while True:
            user_input = input("Option: ")
            choice = int(user_input)
            if (choice < 1 or choice > 2):
                raise ValueError
            return choice
    
    def display_game_over_menu(self, winner):
        print(f"{winner} win")
        
        print("\nHere are your options:\n" +  
              "1. Start a new game.\n" +  
              "2. Quit the game.")  
        while True:
            user_input = input("Option: ")
            choice = int(user_input)
            if (choice < 1 or choice > 2):
                raise ValueError
            return choice