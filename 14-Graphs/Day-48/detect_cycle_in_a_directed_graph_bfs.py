from collections import deque

class Solution:
    def isCyclic(self, V: int, adj: list[list[int]]) -> bool:
        indegree = [0] * V
        for i in range(V):
            for neighbor in adj[i]:
                indegree[neighbor] += 1
                
        queue = deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
                
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return count != V
