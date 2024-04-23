import random

class Node:
    def __init__(self, weight, value, prob, position, move):
        self.weight = weight
        self.value = value
        self.prob = prob
        self.position = position
        self.move = move
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def add_children(self, children):
        self.children.extend(children)
    
    def calc_prob(self):
        # Calculate probability based on chess position evaluation
        # You can use a chess engine or evaluation function here
        return self.prob
    
    def get_child(self, index):
        return self.children[index]
    
    def choose_child(self) -> 'Node':
        # Select child node based on a chess-specific strategy
        # You can use a minimax algorithm or MCTS algorithm here
        total_prob = sum(child.prob for child in self.children)
        rand_val = random.random() * total_prob
        prob_sum = 0
        for child in self.children:
            prob_sum += child.prob
            if prob_sum >= rand_val:
                return child
        return None  # Handle no child chosen case (optional)