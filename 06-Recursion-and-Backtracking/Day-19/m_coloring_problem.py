class Solution:
    def graphColoring(self, graph, k, V):
        color = [0] * V
        
        def is_safe(node, c):
            for i in range(V):
                if graph[node][i] == 1 and color[i] == c:
                    return False
            return True
            
        def solve(node):
            if node == V:
                return True
                
            for c in range(1, k + 1):
                if is_safe(node, c):
                    color[node] = c
                    if solve(node + 1):
                        return True
                    color[node] = 0
                    
            return False
            
        return solve(0)
