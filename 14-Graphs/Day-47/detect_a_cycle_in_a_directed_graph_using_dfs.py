class Solution:
    def isCyclic(self, V: int, adj: list[list[int]]) -> bool:
        visited = [False] * V
        path_visited = [False] * V
        
        def checkCycleDFS(node):
            visited[node] = True
            path_visited[node] = True
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if checkCycleDFS(neighbor):
                        return True
                elif path_visited[neighbor]:
                    return True
                    
            path_visited[node] = False
            return False
            
        for i in range(V):
            if not visited[i]:
                if checkCycleDFS(i):
                    return True
                    
        return False
