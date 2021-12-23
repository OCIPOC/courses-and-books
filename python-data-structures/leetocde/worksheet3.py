from typing import List

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return 'Node=' + str(self.val)




def get_permutations(n: int) -> List[List[int]]:
    from itertools import permutations
    numbers = range(1, n + 1)
    return [list(x) for x in  permutations(numbers)]


def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root



def get_tree_from_list(numbers: list) -> TreeNode:
    if not numbers:
        return None
    else:
        root = TreeNode(numbers.pop(0))
        for x in numbers:
            insert(root, x)
        return root


def print_inorder(root: TreeNode) -> list:
    q, res = [root], []
    while q:
        node = q.pop(0)
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    return res


numbers = get_permutations(3)
print(numbers)
res = [], set_h = set()
for n in numbers:
    res.append(get_tree_from_list(n))

for r in res:
    print(print_inorder(r))