class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
            
        cloned = {}
        
        def dfs(current):
            if current in cloned:
                return cloned[current]
                
            copy = Node(current.val)
            cloned[current] = copy
            
            for neighbor in current.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
            
        return dfs(node)
