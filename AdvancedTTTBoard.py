from TTT9Board import *

class AdvancedTTTBoard(TTT9Board):
    def __init__(self):
        super().__init__()

    def check_win(self, player, board_index):
        # game will only terminate on the last board you played on
        last_board = self.get_board(board_index)

        # if you win one board, you win the game
        if last_board.terminal_state():
            if not last_board.gameDrawn:
                self.overallGameStatus = player
            else:
                self.overallGameStatus = 'd'
                for i in range(3):
                    for j in range(3):
                        if self.gameStatus[i][j] == 'n':
                            self.overallGameStatus = 'n'

        return self.overallGameStatus

    def advanced_terminal_state(self):
        for i in range(3):
            for j in range(3):
                if self.boardArray[i][j].terminal_state():
                    return True

        return False
