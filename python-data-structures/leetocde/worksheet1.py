class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res, stack = [], [root]
        while stack:
            node = stack.pop(0)
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            else:
                res.append('null')
        return ','.join(str(x) for x in res)
            
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(',')
        stack = [TreeNode(int(nodes.pop(0)))]
        
        while nodes:
            node = stack.pop(0)
            node.left = TreeNode(int(nodes.pop(0)))
            stack.append(node.left)
            
            if nodes:
                node.right = TreeNode(int(nodes.pop(0))
                stack.append(node.right)
        return root