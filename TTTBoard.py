

class TTTBoard:
    def __init__(self):
        self.mainBoard = [[' ' for _ in range(3)] for _ in range(3)]
        self.nextPlayer = None
        self.gameOver = False
        self.gameDrawn = False
        self.moveCounter = 0
        self.compChar = None
        self.numX = 0
        self.numO = 0

    def clear_board(self):
        self.mainBoard = [[' ' for _ in range(3)] for _ in range(3)]
        self.gameOver = False
        self.gameDrawn = False
        self.moveCounter = 0
        self.numX = 0
        self.numO = 0

    def new_board(self, oppChar):
        self.clear_board()
        self.compChar = 'X' if oppChar == 'O' else 'O'
        self.nextPlayer = 'X'

    def display_board(self):
        for i in range(3):
            self.print_row(i)
            if i != 2:
                print("------------")

    def print_row(self, n):
        print(" | ".join(self.mainBoard[n]))

    def move_result(self, moveChar, pos):
        boardPos = self.get_coordinates(pos)
        if boardPos:
            self.mainBoard[boardPos[0]][boardPos[1]] = moveChar
            self.moveCounter += 1
            if moveChar == 'X':
                self.numX += 1
            else:
                self.numO += 1
            self.gameOver = self.terminal_state()
            if not self.gameOver:
                self.nextPlayer = 'O' if self.nextPlayer == 'X' else 'X'
        return self

    @staticmethod
    def get_coordinates(boardPos):
        coords = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        if 1 <= boardPos <= 9:
            return coords[boardPos - 1]
        print(f"Error! Position {boardPos} does not Exist!")
        return None

    @staticmethod
    def get_board_position(xval, yval):
        return xval * 3 + yval + 1

    def print_game_result(self):
        if self.gameDrawn:
            print("Game Ended in a Draw!")
        else:
            print(f"Game Over! {self.nextPlayer} wins in {self.moveCounter} moves!")

    def terminal_state(self):
        if self.check_3_in_row(self.nextPlayer):
            return True
        elif self.moveCounter == 9:
            self.gameDrawn = True
            return True
        return False

    def check_3_in_row(self, checkChar, board=None):
        if not board:
            board = self.mainBoard
        for i in range(3):
            if all(board[i][j] == checkChar for j in range(3)):
                return True
            if all(board[j][i] == checkChar for j in range(3)):
                return True
        if all(board[i][i] == checkChar for i in range(3)):
            return True
        if all(board[i][2 - i] == checkChar for i in range(3)):
            return True
        return False

    def applicable_actions(self):
        return [self.get_board_position(i, j)
                for i in range(3) for j in range(3)
                if self.mainBoard[i][j] == ' ']

    def is_move_allowed(self, pos):
        return pos in self.applicable_actions()

    def is_board_full(self):
        return self.moveCounter > 8

    def get_board_fullness(self):
        return self.moveCounter / 9

    def get_advantage(self, player):
        if player == 'X':
            return self.numX - self.numO
        else:
            return self.numO - self.numX

    def get_adjacent_pairs(self, player):
        numPairs = 0
        for i in range(3):
            if self.mainBoard[i][0] == player and self.mainBoard[i][1] == player:
                numPairs += 1
            if self.mainBoard[0][i] == player and self.mainBoard[1][i] == player:
                numPairs += 1
            if self.mainBoard[i][1] == player and self.mainBoard[i][2] == player:
                numPairs += 1
            if self.mainBoard[1][i] == player and self.mainBoard[2][i] == player:
                numPairs += 1
            if self.mainBoard[i][2] == player and self.mainBoard[i][0] == player:
                numPairs += 1
            if self.mainBoard[2][i] == player and self.mainBoard[0][i] == player:
                numPairs += 1
            if self.mainBoard[0][0] == player and self.mainBoard[1][1] == player:
                numPairs += 1
            if self.mainBoard[1][1] == player and self.mainBoard[2][2] == player:
                numPairs += 1
            if self.mainBoard[2][0] == player and self.mainBoard[1][1] == player:
                numPairs += 1
            if self.mainBoard[0][2] == player and self.mainBoard[1][1] == player:
                numPairs += 1
        return numPairs
