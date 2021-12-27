from typing import List, NamedTuple
import math

'''
1. Init sizes list
2. For each element in array
3.  Find all children
4.   For ech child in children 
5.    Find subtree size and add it to subtree sizes list
6.   Mutiply all sizes
7. Add total childrens sizes 
8. Find max
9. Count the number of elements that are equal to max           
'''

class SubTree(NamedTuple):
    root_idx: int
    size: int


def get_sub_trees(idx, parents):
    roots = []


def countHighestScoreNodes(parents: list) -> int:
    res: List[SubTree] = [get_sub_trees(x, parents) for x in  parents] 
    max_val = max(res, key=lambda x: x.size)
    return len([x for x in res if x.size == max_val])






assert countHighestScoreNodes([-1,2,0,2,0]) == 3
assert countHighestScoreNodes([-1,2,0]) == 2
assert countHighestScoreNodes([-1,0]) == 2
assert countHighestScoreNodes([-1,3,3,5,7,6,0,0]) == 2