class Solution:
    def topoSort(self, V: int, adj: list[list[int]]) -> list[int]:
        visited = [False] * V
        stack = []
        
        def dfs(node):
            visited[node] = True
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
                    
            stack.append(node)
            
        for i in range(V):
            if not visited[i]:
                dfs(i)
                
        stack.reverse()
        return stack
