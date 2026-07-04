from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def topView(self, root: TreeNode) -> list[int]:
        if not root:
            return []
            
        hd_node_map = {}
        queue = deque([(root, 0)])
        
        while queue:
            node, hd = queue.popleft()
            
            if hd not in hd_node_map:
                hd_node_map[hd] = node.val
                
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
                
        sorted_hds = sorted(hd_node_map.keys())
        return [hd_node_map[hd] for hd in sorted_hds]
