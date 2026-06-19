class Solution:
    def findPath(self, m, n):
        if m[0][0] == 0 or m[n-1][n-1] == 0:
            return []
            
        result = []
        visited = [[False for _ in range(n)] for _ in range(n)]
        
        di = [1, 0, 0, -1]
        dj = [0, -1, 1, 0]
        directions = ['D', 'L', 'R', 'U']
        
        def solve(row, col, path):
            if row == n - 1 and col == n - 1:
                result.append(path)
                return
                
            for i in range(4):
                next_row = row + di[i]
                next_col = col + dj[i]
                
                if 0 <= next_row < n and 0 <= next_col < n and not visited[next_row][next_col] and m[next_row][next_col] == 1:
                    visited[row][col] = True
                    solve(next_row, next_col, path + directions[i])
                    visited[row][col] = False
                    
        visited[0][0] = True
        solve(0, 0, "")
        return result
