from TTTBoard import *
from MinimaxPlayer import *

class TTTGame:
    def __init__(self):
        self.board = TTTBoard()

    def main(self):
        while True:
            computer_first = False

            comp_move_pos = 0
            opp_move_pos = 0

            print("===============================================================================================================")
            print("Initialized a new game of Tic Tac Toe! (Note that X always plays first)")
            print("Please choose if you want to play \"X\" or \"O\" by typing the desired character:")

            input_char = input().strip().upper()
            while input_char not in ['O', 'X']:
                print("Illegal Input. Please try again.")
                input_char = input().strip().upper()

            self.board.new_board(input_char)

            if input_char == 'O':
                self.board.comp_char = 'X'
                computer_first = True
            else:
                self.board.comp_char = 'O'
                computer_first = False

            comp_player = MinimaxPlayer(self.board)

            if computer_first:
                print("\nNow the computer will play. Using minimax to search for position (1-9) to place a " + self.board.comp_char)
                comp_move_pos = 9
                print(comp_move_pos)
                self.board.move_result(self.board.comp_char, comp_move_pos)

            self.board.display_board()

            while not self.board.gameOver:
                #Opponent plays
                print(f"It is your turn to play, please select a position (1-9) to place a {input_char}")
                opp_move_pos = int(input())

                #Check if move is legal
                while not self.board.is_move_allowed(opp_move_pos):
                    print("That is an illegal move, please choose another board position (1-9)")
                    opp_move_pos = int(input())

                #If the move is legal, execute it on the board
                self.board.move_result(input_char, opp_move_pos)
                print(f"{self.board.nextPlayer} to move next..")
                self.board.display_board()

                if self.board.gameOver:
                    break

                print("\nNow the computer will play. Using minimax to search for position (1-9) to place a " + self.board.comp_char)
                comp_move_pos = comp_player.minimax_decision()

                print("Computer Move: " + str(comp_move_pos))
                self.board.move_result(self.board.comp_char, comp_move_pos)

                if not self.board.gameOver:
                    print(f"{self.board.nextPlayer} to move next..")

                self.board.display_board()

            if self.board.gameOver:
                self.board.print_game_result()

if __name__ == "__main__":
    game = TTTGame()
    game.main()
