import copy
from TTTBoard import *

class TTT9Board:
    def __init__(self):
        self.boardArray = [[TTTBoard(), TTTBoard(), TTTBoard()], [TTTBoard(), TTTBoard(), TTTBoard()], [TTTBoard(), TTTBoard(), TTTBoard()]]
        self.gameStatus = [['n' for _ in range(3)] for _ in range(3)]
        self.firstMove = True
        self.nextPlayer = 'X'
        self.nextBoardIndex = 1
        self.overallGameStatus = 'n'
        self.moveCounter = 0
        self.clear_board()

    def clear_board(self):
        for row in self.boardArray:
            for board in row:
                board.clear_board()
        self.gameStatus = [['n' for _ in range(3)] for _ in range(3)]
        self.moveCounter = 0
        self.nextPlayer = 'X'
        self.overallGameStatus = 'n'
        self.firstMove = True
        self.nextBoardIndex = 1

    def display_board(self):
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    self.boardArray[i][k].print_row(j)  # Print row j of board (i, k)
                    if k != 4:
                        print(" | ", end="")  # Print vertical divider between boards
                print()  # Newline at the end of each row of boards

            if i != 2:
                print("-" * 12 + " | " + "-" * 12 + " | " + "-" * 12)  # Horizontal divider between rows of boards
                print("             |              |             ")  # Spacing between rows of boards

        print()  # Newline at the end of the entire board display

    def get_board(self, index):
        if 1 <= index <= 9:
            return self.boardArray[(index - 1) // 3][(index - 1) % 3]
        print(f"Invalid board number {index} entered.")
        return None

    def get_next_board(self):
        return self.get_board(self.nextBoardIndex)

    def print_win_status(self):
        for i in range(3):
            for j in range(3):
                print(f" {self.gameStatus[i][j]} ", end="")
                if j != 2:
                    print("|", end="")
            if i != 2:
                print("\n------------")
        print()

    def move_result(self, player, boardIndex, boardPos):
        self.get_board(boardIndex).move_result(player, boardPos)
        self.nextBoardIndex = boardPos
        self.moveCounter += 1
        self.check_win(player, boardIndex)
        if self.overallGameStatus == 'n':
            self.nextPlayer = 'O' if self.nextPlayer == 'X' else 'X'
        return self

    def check_win(self, player, boardIndex):
        # Implement the logic for checking the win condition in a subclass
        pass

    def print_game_result(self):
        if self.overallGameStatus == 'X':
            print(f"Game Over! X wins in {self.moveCounter} moves!")
        elif self.overallGameStatus == 'O':
            print(f"Game Over! O wins in {self.moveCounter} moves!")
        elif self.overallGameStatus == 'd':
            print("Game Ended in a Draw!")
        else:
            print("Error, invalid game status")

    def applicable_actions(self):
        possibleMoves = [[0 for _ in range(10)] for _ in range(10)]
        if not self.get_board(self.nextBoardIndex).is_board_full():
            for i in range(3):
                for j in range(3):
                    if self.boardArray[(self.nextBoardIndex - 1) // 3][(self.nextBoardIndex - 1) % 3].mainBoard[i][j] == ' ':
                        possibleMoves[self.nextBoardIndex][TTTBoard.get_board_position(i, j)] = 1
        else:
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        for l in range(3):
                            if self.boardArray[i][j].mainBoard[k][l] == ' ':
                                possibleMoves[TTTBoard.get_board_position(i, j)][TTTBoard.get_board_position(k, l)] = 1
        return possibleMoves

    def is_move_allowed(self, boardIndex, pos):
        if not 1 <= boardIndex <= 9 or not 1 <= pos <= 9:
            return False
        if self.firstMove:
            self.firstMove = False
            return True
        if not self.get_board(boardIndex).is_board_full() and (boardIndex == self.nextBoardIndex or self.get_next_board().is_board_full()):
            return self.get_board(boardIndex).is_move_allowed(pos)
        return False

    # Use Python's deepcopy for cloning objects
    @staticmethod
    def deep_clone(object):
        return copy.deepcopy(object)
