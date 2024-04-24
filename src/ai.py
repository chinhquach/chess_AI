
from board import Board
from piece import Piece
from square import Square
from book import Book
from node import Node

class AI:
    def __init__(self, board, color, depth=3):
        self.board = board
        self.color = color
        self.depth = depth
        self.book = Book()

    def get_best_move(self):
        # Use the book to get the best move
        best_move = self.book.next_move(self.board, self)
        return best_move

    def minimax(self, board, depth, is_maximizing):
        if depth == 0 or board.is_checkmate():
            return self.evaluate(board)

        if is_maximizing:
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
        score = 0
        for square in Square:
            piece = board.piece_at(square)
            if piece is None:
                continue
            value = self.get_piece_value(piece, square)
            if piece.color == self.color:
                score += value
            else:
                score -= value
        return score


    def get_piece_value(self, piece, square):
    # Position values
        position_values = {
            'pawn': [0, 0, 0, 0, 0, 0, 0, 0,
                    5, 5, 5, 5, 5, 5, 5, 5,
                    1, 1, 2, 3, 3, 2, 1, 1,
                    0.5, 0.5, 1, 2.5, 2.5, 1, 0.5, 0.5,
                    0, 0, 0, 2, 2, 0, 0, 0,
                    0.5, -0.5, -1, 0, 0, -1, -0.5, 0.5,
                    0.5, 1, 1, -2, -2, 1, 1, 0.5,
                    0, 0, 0, 0, 0, 0, 0, 0],
            # add similar lists for other piece types
            'knight': [-5, -4, -3, -3, -3, -3, -4, -5,
                       -4, -2, 0, 0, 0, 0, -2, -4,
                       -3, 0, 1, 1.5, 1.5, 1, 0, -3,
                       -3, 0.5, 1.5, 2, 2, 1.5, 0.5, -3,
                       -3, 0, 1.5, 2, 2, 1.5, 0, -3,
                       -3, 0.5, 1, 1.5, 1.5, 1, 0.5, -3,
                       -4, -2, 0, 0.5, 0.5, 0, -2, -4,
                       -5, -4, -3, -3, -3, -3, -4, -5],
            'bishop': [-2, -1, -1, -1, -1, -1, -1, -2,
                       -1, 0, 0, 0, 0, 0, 0, -1,
                       -1, 0, 0.5, 1, 1, 0.5, 0, -1,
                       -1, 0.5, 0.5, 1, 1, 0.5, 0.5, -1,
                       -1, 0, 1, 1, 1, 1, 0, -1,
                       -1, 1, 1, 1, 1, 1, 1, -1,
                       -1, 0.5, 0, 0, 0, 0, 0.5, -1,
                       -2, -1, -1, -1, -1, -1, -1, -2],
            'rook': [0, 0, 0, 0, 0, 0, 0, 0,
                     0.5, 1, 1, 1, 1, 1, 1, 0.5,
                     -0.5, 0, 0, 0, 0, 0, 0, -0.5,
                     -0.5, 0, 0, 0, 0, 0, 0, -0.5,
                     -0.5, 0, 0, 0, 0, 0, 0, -0.5,
                     -0.5, 0, 0, 0, 0, 0, 0, -0.5,
                     -0.5, 0, 0, 0, 0, 0, 0, -0.5,
                     0, 0, 0, 0.5, 0.5, 0, 0, 0],
            'queen': [-2, -1, -1, -0.5, -0.5, -1, -1, -2,
                      -1, 0, 0, 0, 0, 0, 0, -1,
                      -1, 0, 0.5, 0.5, 0.5, 0.5, 0, -1,
                      -0.5, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5,
                      0, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5,
                      -1, 0.5, 0.5, 0.5, 0.5, 0.5, 0, -1,
                      -1, 0, 0.5, 0, 0, 0, 0, -1,
                      -2, -1, -1, -0.5, -0.5, -1, -1, -2],
            'king': [-3, -4, -4, -5, -5, -4, -4, -3,
                     -3, -4, -4, -5, -5, -4, -4, -3,
                     -3, -4, -4, -5, -5, -4, -4, -3,
                     -3, -4, -4, -5, -5, -4, -4, -3,
                     -2, -3, -3, -4, -4, -3, -3, -2,
                     -1, -2, -2, -2, -2, -2, -2, -1,
                     2, 2, 0, 0, 0, 0, 2, 2,
                     2, 3, 1, 0, 0, 1, 3, 2]
        }

        # Get the piece value
        value = piece.value

        # Adjust the value based on the piece's position
        if piece.name in position_values:
            value += position_values[piece.name][square]

        return value























