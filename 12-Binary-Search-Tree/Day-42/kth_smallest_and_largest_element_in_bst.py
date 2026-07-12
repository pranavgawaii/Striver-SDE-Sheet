class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallestLargest(self, root: TreeNode, k: int) -> tuple[int, int]:
        self.count_small = 0
        self.count_large = 0
        self.kth_small = -1
        self.kth_large = -1
        
        def inorder_small(node):
            if not node or self.count_small >= k:
                return
            inorder_small(node.left)
            self.count_small += 1
            if self.count_small == k:
                self.kth_small = node.val
                return
            inorder_small(node.right)
            
        def inorder_large(node):
            if not node or self.count_large >= k:
                return
            inorder_large(node.right)
            self.count_large += 1
            if self.count_large == k:
                self.kth_large = node.val
                return
            inorder_large(node.left)
            
        inorder_small(root)
        inorder_large(root)
        
        return (self.kth_small, self.kth_large)
