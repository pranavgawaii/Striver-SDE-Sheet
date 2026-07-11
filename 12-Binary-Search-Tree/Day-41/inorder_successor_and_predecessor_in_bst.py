class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def predecessorSuccessor(self, root: TreeNode, key: int) -> tuple[TreeNode, TreeNode]:
        pre = None
        suc = None
        
        current = root
        while current:
            if current.val > key:
                suc = current
                current = current.left
            else:
                current = current.right
                
        current = root
        while current:
            if current.val < key:
                pre = current
                current = current.right
            else:
                current = current.left
                
        return (pre, suc)
