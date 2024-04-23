

class AI:
    def __init__(self, color, depth):
        self.color = color
        self.depth = depth

    def get_best_move(self, board):
        best_move = self.minimax(board, self.depth)
        return best_move

    def minimax(self, board, depth, maximizing_player=True):
        if depth == 0 or board.is_game_over():
            return self.evaluate(board)

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax(board, depth - 1, False)
                board.pop()
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
            return max_eval if depth == self.depth else best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax(board, depth - 1, True)
                board.pop()
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
            return min_eval if depth == self.depth else best_move

    def evaluate(self, board):
        # Implement your own evaluation function here
        # This function should assign a score to the board position
        # based on factors like piece values, positional advantages, etc.
        return 0
