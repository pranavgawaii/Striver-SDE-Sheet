class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> list[int]:
        if not root:
            return []
            
        def is_leaf(node):
            return not node.left and not node.right
            
        def add_left_boundary(node, res):
            curr = node.left
            while curr:
                if not is_leaf(curr):
                    res.append(curr.val)
                if curr.left:
                    curr = curr.left
                else:
                    curr = curr.right
                    
        def add_right_boundary(node, res):
            curr = node.right
            temp = []
            while curr:
                if not is_leaf(curr):
                    temp.append(curr.val)
                if curr.right:
                    curr = curr.right
                else:
                    curr = curr.left
            for i in range(len(temp) - 1, -1, -1):
                res.append(temp[i])
                
        def add_leaves(node, res):
            if is_leaf(node):
                res.append(node.val)
                return
            if node.left:
                add_leaves(node.left, res)
            if node.right:
                add_leaves(node.right, res)
                
        result = []
        if not is_leaf(root):
            result.append(root.val)
            
        add_left_boundary(root, result)
        add_leaves(root, result)
        add_right_boundary(root, result)
        
        return result
