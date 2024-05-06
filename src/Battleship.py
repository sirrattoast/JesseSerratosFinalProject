import random

class BattleshipGame:
    def board_info(self, board_size, num_ships):
        self.board_size = board_size
        self.num_ships = num_ships
        self.board = [['O' for _ in range(board_size)] for _ in range(board_size)]
        self.ships = []

    def place_ships(self):
        for _ in range(self.num_ships):
            ship_row = random.randint(0, self.board_size - 1)
            ship_col = random.randint(0, self.board_size - 1)
            while (ship_row, ship_col) in self.ships:
                ship_row = random.randint(0, self.board_size - 1)
                ship_col = random.randint(0, self.board_size - 1)
            self.ships.append((ship_row, ship_col))

    def print_board(self, show_ships=False):
        print("  " + " ".join([str(i) for i in range(self.board_size)]))
        for i in range(self.board_size):
            row = str(i) + " "
            for j in range(self.board_size):
                if not show_ships and (i, j) in self.ships:
                    row += 'O '
                else:
                    row += self.board[i][j] + " "
            print(row)

    def check_guess(self, guess_row, guess_col):
        if (guess_row, guess_col) in self.ships:
            self.board[guess_row][guess_col] = 'X'
            print("Good shot! Enemy ship sank!")
            self.ships.remove((guess_row, guess_col))
            if not self.ships:
                print("Hey! You sank all my ships... ( ɵ̥__ɵ̥)")
                print("YOU WIN!!!")
                return True
            else:
                return False
        else:
            self.board[guess_row][guess_col] = 'X'
            print("Sorry, you missed.")
            return False

    def ai_guess(self):
        guess_row = random.randint(0, self.board_size - 1)
        guess_col = random.randint(0, self.board_size - 1)
        return guess_row, guess_col

def main():
    print("Wanna play battleship?")
    board_size = 5
    while True:
        try:
            num_ships = int(input("Enter the number of ships(1-25): "))
            if num_ships > 25:
                print("Too many ships in the sea! Please keep it to 1-25. :)")
                continue
            if num_ships <= 0:
                print("Hey, where'd your ships go? Please keep it to 1-25. :)")
                continue
            if num_ships <= 25:
                print ("Ships are placed, lets play!")
                break
        except ValueError:
            print("Please enter a valid number.")

    player_game = BattleshipGame(board_size, num_ships)
    player_game.place_ships()

    Battleship = BattleshipGame(board_size, num_ships)
    Battleship.place_ships()

    while True:
        print("\nPlayer's Turn:")
        player_game.print_board(show_ships=True)
        try:
            guess_row = int(input("Guess Row: "))
            guess_col = int(input("Guess Col: "))
            if guess_row < 0 or guess_row >= board_size or guess_col < 0 or guess_col >= board_size:
                print("Woops! Your strike's out of range! Try again!")
                continue
            if player_game.check_guess(guess_row, guess_col):
                break
        except ValueError:
            print("Please enter a valid number.")

        print("\nAI's Turn:")
        ai_guess_row, ai_guess_col = Battleship.ai_guess()
        print(f"Hmmm, i'll strike row {ai_guess_row} and column {ai_guess_col}.")
        if Battleship.check_guess(ai_guess_row, ai_guess_col):
            break

if __name__ == "__main__":
    main()