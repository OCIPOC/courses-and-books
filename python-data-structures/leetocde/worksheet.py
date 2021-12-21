class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_bst(array: list, index=-1) -> TreeNode:
    if not array:
        return None
    else:
        index = len(array) // 2 if index == -1 else index
        node = TreeNode(array[index])
        node.left = create_bst(array[:index])
        node.right = create_bst(array[index+1:])
        return node
   
def inorder(node: TreeNode) -> list:
    if not node:
        return []
    else:
        return inorder(node.left) + [node.val] + inorder(node.right)
        


root = create_bst([1, 2, 3, 4, 15])
print(inorder(root))