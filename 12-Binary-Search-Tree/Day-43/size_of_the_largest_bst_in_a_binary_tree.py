class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class NodeValue:
    def __init__(self, min_node, max_node, max_size):
        self.min_node = min_node
        self.max_node = max_node
        self.max_size = max_size

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def largest_bst_helper(node):
            if not node:
                return NodeValue(float('inf'), float('-inf'), 0)
                
            left = largest_bst_helper(node.left)
            right = largest_bst_helper(node.right)
            
            if left.max_node < node.val < right.min_node:
                return NodeValue(
                    min(node.val, left.min_node),
                    max(node.val, right.max_node),
                    left.max_size + right.max_size + 1
                )
                
            return NodeValue(
                float('-inf'),
                float('inf'),
                max(left.max_size, right.max_size)
            )
            
        return largest_bst_helper(root).max_size
