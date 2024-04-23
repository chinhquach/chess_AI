from node import Node
from ai import AI

class Book:
    def __init__(self):
        self.root = self._create()

    def _create(self):
        # Create a new Node instance and return it
        root = Node(weight=0, value=0, prob=1)
        return root

    def next_move(self, board):
        # Create an instance of the AI class
        ai = AI()

        # Use the AI instance to get the next move based on the current board state
        next_move = ai.get_next_move(board)

        return next_move