class Solution:
    def dfsOfGraph(self, V: int, adj: list[list[int]]) -> list[int]:
        result = []
        visited = [False] * V
        
        def dfs(node):
            visited[node] = True
            result.append(node)
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
                    
        dfs(0)
        return result
