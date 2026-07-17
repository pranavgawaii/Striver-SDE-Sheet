from collections import deque

class Solution:
    def isCycle(self, V: int, adj: list[list[int]]) -> bool:
        visited = [False] * V
        
        def checkCycleBFS(start):
            queue = deque([(start, -1)])
            visited[start] = True
            
            while queue:
                node, parent = queue.popleft()
                
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, node))
                    elif parent != neighbor:
                        return True
                        
            return False
            
        for i in range(V):
            if not visited[i]:
                if checkCycleBFS(i):
                    return True
                    
        return False
