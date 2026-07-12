class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def floorInBST(self, root: TreeNode, X: int) -> int:
        floor_val = -1
        current = root
        
        while current:
            if current.val == X:
                return current.val
            elif current.val > X:
                current = current.left
            else:
                floor_val = current.val
                current = current.right
                
        return floor_val
