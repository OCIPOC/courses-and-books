import math

class Node:
    def __init__(self, right, left) -> None:
        self.left: Node = left
        self.right: Node = right
        

def build_tree(nodes: list) -> Node:
    q = [0]
    root = Node()
    while q:
        




def get_highest_score_nodes(nodes: list) -> int:
    pass

assert(get_highest_score_nodes([-1,2,0,2,0]) == 3)
assert(get_highest_score_nodes([-1,2,0]) == 2)
assert(get_highest_score_nodes([-1,0]) == 2)
assert(get_highest_score_nodes([-1,3,3,5,7,6,0,0]) == 2)