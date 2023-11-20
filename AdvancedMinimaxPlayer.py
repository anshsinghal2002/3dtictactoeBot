import copy
import random

class AdvancedMinimaxPlayer:
    def __init__(self, game, depth_cutoff):
        self.current_game = game.board
        self.game = game
        self.search_state_board = None
        self.recursion_num = 0
        self.total_states = 0
        self.reached_terminal_state = False
        self.depth_cutoff = depth_cutoff

    def get_state_utility(self, state_board_gsu):
        if state_board_gsu.overallGameStatus == 'd':
            return 5
        elif (state_board_gsu.overallGameStatus == 'X' and self.game.p2_char == 'X') or (state_board_gsu.overallGameStatus == 'O' and self.game.p2_char == 'O'):
            return 50
        elif (state_board_gsu.overallGameStatus == 'X' and self.game.p2_char == 'O') or (state_board_gsu.overallGameStatus == 'O' and self.game.p2_char == 'X'):
            return -50
        print("Overall Game Status: ", state_board_gsu.overallGameStatus)
        return 2

    def heuristic_evaluation(self, state_board_hf):
        h_val = 0
        for i in range(3):
            for j in range(3):
                board_advantage = state_board_hf.boardArray[i][j].get_advantage(state_board_hf.nextPlayer)
                adjacency_advantage = state_board_hf.boardArray[i][j].get_adjacent_pairs(state_board_hf.nextPlayer)
                h_val += board_advantage * adjacency_advantage
        return h_val

    def cutoff_test(self, state_board_cf):
        if state_board_cf.overallGameStatus != 'n':
            self.reached_terminal_state = True
            return self.reached_terminal_state
        if self.recursion_num < self.depth_cutoff:
            return False
        return True

    def h_minimax_decision(self):
        best_move = self.random_move()
        updated_utility = False
        best_move_utility = -100

        self.total_states = 0
        self.search_state_board = copy.deepcopy(self.current_game)
        possible_moves = self.search_state_board.applicable_actions()

        v = self.max_value(self.search_state_board, -100, 100)
        best_move_utility = v

        for i in range(1, len(possible_moves)):
            for j in range(1, len(possible_moves[i])):
                if possible_moves[i][j] != 0:
                    self.search_state_board = copy.deepcopy(self.current_game)
                    self.recursion_num = 0
                    self.reached_terminal_state = False

                    move_utility = self.min_value(self.search_state_board.move_result(self.search_state_board.nextPlayer, i, j), -100, 100)

                    if move_utility >= best_move_utility:
                        best_move_utility = move_utility
                        updated_utility = True
                        best_move = [i, j]

        if not updated_utility:
            print("Did not update utility - playing Random Move")

        return best_move

    def max_value(self, state_board_max, alpha, beta):
        self.recursion_num += 1
        if self.cutoff_test(state_board_max):
            if self.reached_terminal_state:
                self.total_states += 1
                self.reached_terminal_state = False
                return self.get_state_utility(state_board_max)
            else:
                return self.heuristic_evaluation(state_board_max)

        v = -100
        possible_moves = state_board_max.applicable_actions()

        for i in range(1, 10):
            for j in range(1, 10):
                if possible_moves[i][j] != 0:
                    temp_board = copy.deepcopy(state_board_max)
                    v = max(v, self.min_value(temp_board.move_result(temp_board.nextPlayer, i, j), alpha, beta))
                    if v >= beta:
                        return v
                    alpha = max(alpha, v)

        return v

    def min_value(self, state_board_min, alpha, beta):
        self.recursion_num += 1
        if self.cutoff_test(state_board_min):
            if self.reached_terminal_state:
                self.total_states += 1
                self.reached_terminal_state = False
                return self.get_state_utility(state_board_min)
            else:
                return self.heuristic_evaluation(state_board_min)

        v = 100
        possible_moves = state_board_min.applicable_actions()

        for i in range(1, 10):
            for j in range(1, 10):
                if possible_moves[i][j] != 0:
                    temp_board = copy.deepcopy(state_board_min)
                    v = min(v, self.max_value(temp_board.move_result(temp_board.nextPlayer, i, j), alpha, beta))
                    if v <= alpha:
                        return v
                    beta = min(beta, v)

        return v

    def random_move(self):
        board_num = self.current_game.nextBoardIndex
        local_board = self.current_game.get_next_board()

        if local_board.is_board_full():
            for i in range(1, 10):
                local_board = self.current_game.get_board(i)
                if not local_board.is_board_full():
                    board_num = i
                    break

        while True:
            move_pos = random.randint(1, 9)
            if self.current_game.is_move_allowed(board_num, move_pos):
                break

        return [board_num, move_pos]

