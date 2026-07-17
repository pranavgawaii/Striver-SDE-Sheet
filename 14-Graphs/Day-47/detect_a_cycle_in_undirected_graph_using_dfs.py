class Solution:
    def isCycle(self, V: int, adj: list[list[int]]) -> bool:
        visited = [False] * V
        
        def checkCycleDFS(node, parent):
            visited[node] = True
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if checkCycleDFS(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
                    
            return False
            
        for i in range(V):
            if not visited[i]:
                if checkCycleDFS(i, -1):
                    return True
                    
        return False
