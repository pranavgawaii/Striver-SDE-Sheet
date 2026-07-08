class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.postorder_index = len(postorder) - 1
        
        def array_to_tree(left, right):
            if left > right:
                return None
                
            root_value = postorder[self.postorder_index]
            root = TreeNode(root_value)
            
            self.postorder_index -= 1
            
            root.right = array_to_tree(inorder_map[root_value] + 1, right)
            root.left = array_to_tree(left, inorder_map[root_value] - 1)
            
            return root
            
        return array_to_tree(0, len(inorder) - 1)
