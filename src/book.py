from node import Node
from ai import AI

class Book:
    def __init__(self):
        self.root = self._create()

    def _create(self):
        # Create a decision tree to store data and strategies
        root = Node(weight=0, value=0, prob=1)
        return root

    def next_move(self, board, ai):
        # Use AI instance to get the next move based on the current state of the board
        next_move = ai.get_best_move(board)
        return next_move

    def learn(self, game_history):
        # This function will be called after each game to learn from the game history
        # For example: update the decision tree based on the good and bad moves made in the game
        for move in game_history:
            # Perform decision tree update based on the move in the game history
            self.update_decision_tree(move)
    
    def update_decision_tree(self, move):
        # Update the decision tree based on the move
        # For example: increase the weight of the node corresponding to the move made
        node = self.find_node(move)
        if node:
            node.weight += 1
    
    def find_node(self, move):
        # This function should find and return the node corresponding to the given move
        # You need to implement this function based on your decision tree structure
        pass

    def save_to_file(self, filename):
        # Save the decision tree and related data to a file for future use
        # This can be useful for performance optimization and maintaining the state of the AI
        with open(filename, 'w') as file:
            self._save_node(self.root, file)
    
    def _save_node(self, node, file):
        if node is None:
            return
        # Save the node's weight, value, and probability to the file
        file.write(f"{node.weight},{node.value},{node.prob}\n")
        # Recursively save the left and right child nodes
        self._save_node(node.left, file)
        self._save_node(node.right, file)