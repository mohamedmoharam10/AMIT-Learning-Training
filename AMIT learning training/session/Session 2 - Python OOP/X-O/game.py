import player
import board
import menu

class Game:
    def  __init__(self):
        self.players = [player.Player(), player.Player()]
        self.board = board.Board()
        self.menu_screen = menu.Menu()
        self.current_player_index = 0
    
    def start_game(self):
        """Starts the game by displaying the main menu and calling the appropriate method based on user's choice"""
        player_choice = self.menu_screen.display_main_menu()

        if player_choice == 1:
            self.setup_players()
            self.play_game()
        
        else:
            self.quit_game()
    
    def setup_players(self):
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number}")
            player.choose_name()
            if number == 1:
                player.set_symbol()
            else:
                if self.players[0].symbol == 'X':
                    self.players[1].symbol = 'O'
                else:
                    self.players[1].symbol = 'X'

                print(f"\nWelcome {self.players[1].name}! You will be playing as '{self.players[1].symbol}'")
            

            print('-' * 20)

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choise = self.menu_screen.display_game_over_menu(self.players[1 - self.current_player_index].name)
                if choise == 1:
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def quit_game(self):
        print("Game Over!")
	
    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s Turn")
        while True:
            try:
                cell_choice = int(input("Chose a cell (1-9)"))  # k
                if 1 <= cell_choice <=9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print('Invalid Move, Try Again!')
            except ValueError:
                print('Please enter a number between 1 and 9.')
	
        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index


    def check_win(self):
        winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
                   [0, 3, 6], [1, 4, 7], [2, 5, 8], 
                   [0, 4, 8], [2, 4, 6]]
                   
        for w in winning:
            if self.board.board[w[0]] == self.board.board[w[1]] == self.board.board[w[2]]:
                return True

        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)


    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

Game().start_game()