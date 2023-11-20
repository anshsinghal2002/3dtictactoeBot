import copy

class BasicMinimaxPlayer:
    def __init__(self, curr_game):
        self.current_game = curr_game
        self.search_state_board = None
        self.recursion_num = 0
        self.total_states = 0
        print("Computer Player Instantiated!")

    def get_state_utility(self, state_board):
        if state_board.game_drawn:
            return 0
        if state_board.next_player == state_board.comp_char:
            return 10
        else:
            return -10

    def minimax_decision(self):
        best_move = 0
        best_move_utility = -100
        self.recursion_num = 0
        self.total_states = 0

        self.search_state_board = copy.deepcopy(self.current_game)
        possible_moves = self.search_state_board.applicable_actions()

        for i in range(1, len(possible_moves)):
            if possible_moves[i] != 0:
                self.search_state_board = copy.deepcopy(self.current_game)
                a = possible_moves[i]

                move_utility = self.min_value(self.search_state_board.move_result(self.search_state_board.next_player, a))

                if move_utility > best_move_utility:
                    best_move = possible_moves[i]
                    best_move_utility = move_utility

        return best_move

    def max_value(self, state_board):
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

                v = max(v, self.min_value(temp_board.move_result(temp_board.next_player, a)))

        return v

    def min_value(self, state_board):
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

                v = min(v, self.max_value(temp_board.move_result(temp_board.next_player, a)))

        return v
