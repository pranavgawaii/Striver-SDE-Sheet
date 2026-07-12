class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findCeil(self, root: TreeNode, X: int) -> int:
        ceil_val = -1
        current = root
        
        while current:
            if current.val == X:
                return current.val
            elif current.val < X:
                current = current.right
            else:
                ceil_val = current.val
                current = current.left
                
        return ceil_val
