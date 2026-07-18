from collections import deque

class Solution:
    def topoSort(self, V: int, adj: list[list[int]]) -> list[int]:
        indegree = [0] * V
        for i in range(V):
            for neighbor in adj[i]:
                indegree[neighbor] += 1
                
        queue = deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
                
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return result
