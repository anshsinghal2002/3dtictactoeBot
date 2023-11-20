import sys
from TTTBoard import *
from MinimaxPlayer import *

class TTTGame:
    def __init__(self):
        # Instantiate the board
        self.board = TTTBoard()

    def main(self):
        # Main outer loop always runs
        while True:
            # Boolean to keep track of who plays first
            computer_first = False

            # Integers to record the board position specified by the opponent and computer
            comp_move_pos = 0
            opp_move_pos = 0

            # Set up input stream using System in
            print("===============================================================================================================")
            print("Initialized a new game of Tic Tac Toe! (Note that X always plays first)")
            print("Please choose if you want to play \"X\" or \"O\" by typing the desired character:")

            input_char = input().strip().upper()  # Read and process the input character
            while input_char not in ['O', 'X']:
                print("Illegal Input. Please try again.")
                input_char = input().strip().upper()

            # Set up a new board
            self.board.new_board(input_char)

            # Determine who plays first
            if input_char == 'O':
                self.board.comp_char = 'X'
                computer_first = True
            else:
                self.board.comp_char = 'O'
                computer_first = False

            # Instantiate Minimax computer player
            comp_player = MinimaxPlayer(self.board)

            # Check if computer plays first
            if computer_first:
                print("\nNow the computer will play. Using minimax to search for position (1-9) to place a " + self.board.comp_char)
                comp_move_pos = 9
                print(comp_move_pos)
                self.board.move_result(self.board.comp_char, comp_move_pos)

            self.board.display_board()  # Display the board

            # Main game playing loop
            while not self.board.gameOver:
                # Opponent plays
                print(f"It is your turn to play, please select a position (1-9) to place a {input_char}")
                opp_move_pos = int(input())

                # Check if move is legal
                while not self.board.is_move_allowed(opp_move_pos):
                    print("That is an illegal move, please choose another board position (1-9)")
                    opp_move_pos = int(input())

                # If the move is legal, execute it on the board
                self.board.move_result(input_char, opp_move_pos)
                print(f"{self.board.nextPlayer} to move next..")  # Display who's move it is next
                self.board.display_board()  # Display the board

                # Check if game is over to break out of inner while loop
                if self.board.gameOver:
                    break

                # Computer's turn
                print("\nNow the computer will play. Using minimax to search for position (1-9) to place a " + self.board.comp_char)
                comp_move_pos = comp_player.minimax_decision()

                # Output move
                print("Computer Move: " + str(comp_move_pos))
                self.board.move_result(self.board.comp_char, comp_move_pos)

                # Display who's move it is
                if not self.board.gameOver:
                    print(f"{self.board.nextPlayer} to move next..")

                self.board.display_board()  # Display the board

            # Print result if the game is over
            if self.board.gameOver:
                self.board.print_game_result()

if __name__ == "__main__":
    game = TTTGame()
    game.main()
