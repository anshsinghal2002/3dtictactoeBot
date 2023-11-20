class UltimateTicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(9)] for _ in range(9)]
        self.current_board = (1, 1)

    def print_board(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print('-' * 25)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print('|', end=' ')
                print(self.board[i][j], end=' ')
            print()

    def make_move(self, position, symbol):
        row, col = position
        if self.board[row][col] == ' ' and self.check_mini_board_full(position):
            self.board[row][col] = symbol
            self.current_board = (row % 3, col % 3)
            return True
        else:
            return False

    def check_mini_board_full(self, position):
        row, col = position
        mini_board = self.board[row][col]
        for i in range(row - row % 3, row - row % 3 + 3):
            for j in range(col - col % 3, col - col % 3 + 3):
                if self.board[i][j] != mini_board and self.board[i][j] == ' ':
                    return False
        return True

    def check_winner(self):
        for i in range(3):
            #check rows and columns for three consecutive wins
            if (self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ' or
                self.board[0][i] == self.board[1][i] == self.board[2][i] != ' '):
                return True, self.board[i][i]

        #check diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ' or
            self.board[0][2] == self.board[1][1] == self.board[2][0] != ' '):
            return True, self.board[1][1]

        #check for three boards in a row win
        win_conditions = [
            [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],  # Rows
            [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],  # Columns
            [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]  # Diagonals
        ]
        for condition in win_conditions:
            symbols = [self.board[row][col] for row, col in condition]
            if symbols.count('O') == 3:
                return True, 'O'
            elif symbols.count('X') == 3:
                return True, 'X'

        return False, None


    def is_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def reset_board(self):
        self.board = [[' ' for _ in range(9)] for _ in range(9)]
        self.current_board = (1, 1)


game = UltimateTicTacToe()
game.print_board()

current_symbol = 'X'

while True:
    try:
        row, col = game.current_board
        print(f"Player {current_symbol}, enter your position for mini board [{row},{col}] (0-8): ")
        position = int(input())
        position = (row * 3 + position // 3, col * 3 + position % 3)

        if not (0 <= position[0] <= 8) or not (0 <= position[1] <= 8):
            print("Please enter a valid position (0-8).")
            continue
        if not game.make_move(position, current_symbol):
            print("That position is already taken or the mini board is full. Try again.")
            continue

        game.print_board()

        winner_found, winner_symbol = game.check_winner()
        if winner_found:
            print(f"Player {winner_symbol} wins!")
            break
        elif game.is_full():
            print("It's a tie!")
            break

        current_symbol = 'O' if current_symbol == 'X' else 'X'

    except ValueError:
        print("Please enter a valid position (0-8).")
