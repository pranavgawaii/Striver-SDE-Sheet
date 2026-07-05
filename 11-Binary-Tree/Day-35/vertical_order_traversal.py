from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
            
        nodes_map = defaultdict(lambda: defaultdict(list))
        queue = deque([(root, 0, 0)])
        
        while queue:
            node, row, col = queue.popleft()
            nodes_map[col][row].append(node.val)
            
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))
                
        result = []
        for col in sorted(nodes_map.keys()):
            col_vals = []
            for row in sorted(nodes_map[col].keys()):
                col_vals.extend(sorted(nodes_map[col][row]))
            result.append(col_vals)
            
        return result
