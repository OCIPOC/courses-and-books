import time
from typing import List

class TreeNode:
    def __init__(self, value, parent=None, children=[]):
        self.value = value
        self.parent: TreeNode = parent
        self.children: List[TreeNode] = children


root = TreeNode(0)
left = TreeNode(1, root)
right = TreeNode(2, root)
right_left = TreeNode(3, right)
right.children.append(right_left)
root.children = [left, right]


def preorder(node: TreeNode) -> str: 
    print(node.value)
    time.sleep(1)
    if not node:
        return ''
    else:
        res = [str(node.value)]
        for child in node.children:
            res.append(preorder(child))
        return ''.join(res)
        

print(preorder(root))


d = {}
for k, v in d.items():
    print(k, v)