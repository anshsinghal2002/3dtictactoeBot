import copy

class MinimaxPlayer:
    def __init__(self, curr_game):
        self.current_game = curr_game
        self.search_state_board = None
        self.recursion_num = 0
        self.total_states = 0
        print("Computer Player Instantiated!")

    def get_state_utility(self, state_board):
        if state_board.gameDrawn:
            return 0
        if state_board.nextPlayer == state_board.comp_char:
            return 10
        else:
            return -10

    def minimax_decision(self):
        best_move = 0
        move_utility = -100
        self.total_states = 0
        self.recursion_num = 0

        self.search_state_board = copy.deepcopy(self.current_game)
        possible_moves = self.search_state_board.applicable_actions()

        v = self.max_value(self.search_state_board, -100, 100)

        for i in range(1, len(possible_moves)):
            if possible_moves[i] != 0:
                self.search_state_board = copy.deepcopy(self.current_game)
                a = possible_moves[i]

                move_utility = self.min_value(self.search_state_board.move_result(self.search_state_board.nextPlayer, a), -100, 100)

                if move_utility == v:
                    best_move = possible_moves[i]
                    return best_move

        return best_move

    def max_value(self, state_board, alpha, beta):
        self.recursion_num += 1

        if state_board.terminal_state():
            self.total_states += 1
            return self.get_state_utility(state_board)

        v = -100
        possible_moves = state_board.applicable_actions()

        for i in range(1, len(possible_moves)):
            if possible_moves[i] != 0:
                temp_board = copy.deepcopy(state_board)
                a = possible_moves[i]

                v = max(v, self.min_value(temp_board.move_result(temp_board.nextPlayer, a), alpha, beta))

                if v >= beta:
                    return v

                alpha = max(alpha, v)

        return v

    def min_value(self, state_board, alpha, beta):
        self.recursion_num += 1

        if state_board.terminal_state():
            self.total_states += 1
            return self.get_state_utility(state_board)

        v = 100
        possible_moves = state_board.applicable_actions()

        for i in range(1, len(possible_moves)):
            if possible_moves[i] != 0:
                temp_board = copy.deepcopy(state_board)
                a = possible_moves[i]

                v = min(v, self.max_value(temp_board.move_result(temp_board.nextPlayer, a), alpha, beta))

                if v <= alpha:
                    return v

                beta = min(beta, v)

        return v
