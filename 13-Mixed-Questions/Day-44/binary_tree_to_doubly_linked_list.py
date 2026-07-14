class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bToDLL(self, root: TreeNode) -> TreeNode:
        self.head = None
        self.prev = None
        
        def inorder(node):
            if not node:
                return
                
            inorder(node.left)
            
            if not self.prev:
                self.head = node
            else:
                self.prev.right = node
                node.left = self.prev
                
            self.prev = node
            
            inorder(node.right)
            
        inorder(root)
        return self.head
