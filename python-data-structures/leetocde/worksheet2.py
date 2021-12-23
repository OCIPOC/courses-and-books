class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root: TreeNode) -> list:
    pass


def create_from_list(nodes: list) -> TreeNode:
    if not nodes:
        return None
    else:
        mid = len(nodes) // 2
        return TreeNode(nodes[mid], create_from_list(nodes[0: mid-1]), create_from_list(nodes[mid+1:]))


def create_from_list(nodes: list) -> TreeNode:
    if not nodes:
        return None
    else:
        mid = len(nodes) // 2
        return TreeNode(nodes[mid], create_from_list(nodes[0: mid-1]), create_from_list(nodes[mid+1:]))
    


def create_all_variants(root: TreeNode) -> list:
    # get ordered list 
    nodes = inorder(root)   
    return create_from_list(nodes)




def create_permutations(self, numbers: list) -> list:
        import itertools
        return list(itertools.permutations(numbers))
          
    
    
    def create_tree(self, n: list, root: TreeNode=None) -> TreeNode:
                    
        if n and not root:
            root = TreeNode(n[0])
            self.create_tree(n[1:], root)
        if n and root.val > n[0]:
            root.left = TreeNode(n[0])
            temp_n = [x for x in n if x < n[0]]
            self.create_tree(temp_n, root.left)
        elif n:
            root.right = TreeNode(n[0])
            temp_n = [x for x in n if x > n[0]]
            self.create_tree(temp_n, root.right)
        return root




