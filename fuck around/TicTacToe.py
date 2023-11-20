class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Create an empty board

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            print('-------------')

    def make_move(self, position, symbol):
        if self.board[position] == ' ':
            self.board[position] = symbol
            return True
        else:
            return False

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return True, self.board[condition[0]]
        return False, None

    def is_board_full(self):
        return ' ' not in self.board

    def reset_board(self):
        self.board = [' ' for _ in range(9)]


# Example usage:
game = TicTacToe()
game.print_board()

current_symbol = 'X'

while True:
    try:
        position = int(input(f"Player {current_symbol}, enter your position (0-8): "))
        if not (0 <= position <= 8):
            print("Please enter a valid position (0-8).")
            continue
        if not game.make_move(position, current_symbol):
            print("That position is already taken. Try again.")
            continue

        game.print_board()

        winner_found, winner_symbol = game.check_winner()
        if winner_found:
            print(f"Player {winner_symbol} wins!")
            break
        elif game.is_board_full():
            print("It's a tie!")
            break

        current_symbol = 'O' if current_symbol == 'X' else 'X'

    except ValueError:
        print("Please enter a valid position (0-8).")
