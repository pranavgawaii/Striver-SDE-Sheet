class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root, is_reverse):
        self.stack = []
        self.is_reverse = is_reverse
        self.push_all(root)

    def next(self):
        node = self.stack.pop()
        if not self.is_reverse:
            self.push_all(node.right)
        else:
            self.push_all(node.left)
        return node.val

    def push_all(self, node):
        while node:
            self.stack.append(node)
            if not self.is_reverse:
                node = node.left
            else:
                node = node.right

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
            
        left_iterator = BSTIterator(root, False)
        right_iterator = BSTIterator(root, True)
        
        left_val = left_iterator.next()
        right_val = right_iterator.next()
        
        while left_val < right_val:
            current_sum = left_val + right_val
            if current_sum == k:
                return True
            elif current_sum < k:
                left_val = left_iterator.next()
            else:
                right_val = right_iterator.next()
                
        return False
