import copy
from AdvancedTTTBoard import *
from AdvancedMinimaxPlayer import *

class AdvancedTTTGame:
    def __init__(self):
        self.board = AdvancedTTTBoard()
        self.p2_char = ' '

    def main(self):
        game = AdvancedTTTGame()
        depth_cutoff = int(input("Decide the difficulty by entering a number 1 - 10 (The lower the number, the easier the game): "))

        while True:
            p1_first = True
            p1_move = ""
            p2_move = [2, 2]
            is_move_allowed = False

            print(
                "===============================================================================================================")
            print("Initialized a new game of Advanced Tic Tac Toe! (Note that X always plays first)")
            print("Please choose if you want to play \"X\" or \"O\" by typing the desired character:")

            p1_char = input().strip().upper()
            while p1_char not in ['O', 'X']:
                print("Illegal Input. Please try again.")
                p1_char = input().strip().upper()

            if p1_char == 'O':
                p1_first = False
                game.p2_char = 'X'
            elif p1_char == 'X':
                p1_first = True
                game.p2_char = 'O'
            else:
                print("Oh god this should never happen please help")

            comp_player = AdvancedMinimaxPlayer(game, depth_cutoff)

            if not p1_first:
                print("Computer playing first")
                game.board.move_result(game.p2_char, p2_move[0], p2_move[1])
                game.board.first_move = False
                print(f"{p2_move[0]} {p2_move[1]}")

            while game.board.overallGameStatus == 'n':
                game.board.display_board()

                # Human player plays
                if game.board.first_move or game.board.get_next_board().is_board_full():
                    helpful_hint = "You can play on any board."
                else:
                    helpful_hint = f"You should play on board {game.board.nextBoardIndex}."

                print(f"It is your turn to play, please enter the board (1-9) you would like to play on followed by"
                      f" the position on that board (1-9). {helpful_hint}")

                # Read user input
                p1_move = input()

                # Splitting the input and ensuring it has two parts
                p1_move_parts = p1_move.split()

                while len(p1_move_parts) != 2 or not p1_move_parts[0].isdigit() or not p1_move_parts[1].isdigit():
                    print("Invalid Input. Moves should be entered as two digits from 1-9 separated by a space")
                    p1_move = input()
                    p1_move_parts = p1_move.split()

                board_index = int(p1_move_parts[0])
                board_pos = int(p1_move_parts[1])

                # Check if entered move is a valid move
                while not game.board.is_move_allowed(board_index, board_pos):
                    print("Illegal Input. Please try again.")
                    p1_move = input()
                    board_index = int(p1_move.split()[0])
                    board_pos = int(p1_move.split()[1])

                game.board.move_result(p1_char, board_index, board_pos)
                print(f"You just made move {board_index} {board_pos}")

                if game.board.overallGameStatus != 'n':
                    break

                # Computer makes move
                computer_move = comp_player.h_minimax_decision()
                print(f"{computer_move[0]} {computer_move[1]}")
                game.board.move_result(game.p2_char, computer_move[0], computer_move[1])

                print(f"Computer player just made move {computer_move[0]} {computer_move[1]}")

            # After loop terminates, print the game result
            game.board.print_game_result()
            game.board.display_board()
            game.board.clear_board()


if __name__ == "__main__":
    advancedGame = AdvancedTTTGame()
    advancedGame.main()

