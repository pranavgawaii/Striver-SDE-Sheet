from collections import deque

class Solution:
    def bfsOfGraph(self, V: int, adj: list[list[int]]) -> list[int]:
        result = []
        visited = [False] * V
        
        queue = deque([0])
        visited[0] = True
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    
        return result
