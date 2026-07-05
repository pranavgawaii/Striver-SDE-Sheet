from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
            
        max_width = 0
        queue = deque([(root, 0)])
        
        while queue:
            level_length = len(queue)
            _, first_idx = queue[0]
            last_idx = first_idx
            
            for _ in range(level_length):
                node, idx = queue.popleft()
                last_idx = idx
                
                if node.left:
                    queue.append((node.left, 2 * idx + 1))
                if node.right:
                    queue.append((node.right, 2 * idx + 2))
                    
            max_width = max(max_width, last_idx - first_idx + 1)
            
        return max_width
