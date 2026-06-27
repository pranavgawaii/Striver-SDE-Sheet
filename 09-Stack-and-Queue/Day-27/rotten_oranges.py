from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh_count += 1
                    
        if fresh_count == 0:
            return 0
            
        max_time = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while q:
            r, c, time = q.popleft()
            max_time = max(max_time, time)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    q.append((nr, nc, time + 1))
                    
        if fresh_count > 0:
            return -1
            
        return max_time
