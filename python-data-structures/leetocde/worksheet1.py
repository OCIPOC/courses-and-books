class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def from_list(tree: list, root: TreeNode=None):
    if not tree:
        return None
    elif not root:
        root = TreeNode(tree.pop(0))
        return from_list(tree, root)
    else:
        root.left = TreeNode(tree.pop(0))
        root.right = TreeNode(tree.pop(0))
        from_list(tree, root.left)
        from_list(tree, root.right)

    return root


def bf_to_list(node: TreeNode):
    res, q = [], [node]
    while q:
        tmp: TreeNode = q.pop(0)
        if tmp:
            res.append(tmp.val)
            q.append(tmp.left)
            q.append(tmp.right)
    return res


root = from_list([5, 1, 4, None, None, 3, 6])
print(bf_to_list(root))


print([1, 2, 3].index(2))