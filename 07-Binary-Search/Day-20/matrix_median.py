class Solution:
    def median(self, matrix: list[list[int]], R: int, C: int) -> int:
        def countSmallerThanMid(row, mid):
            l = 0
            h = len(row) - 1
            while l <= h:
                m = (l + h) // 2
                if row[m] <= mid:
                    l = m + 1
                else:
                    h = m - 1
            return l
            
        low = 1
        high = 10**9
        
        for i in range(R):
            low = min(low, matrix[i][0])
            high = max(high, matrix[i][C-1])
            
        req = (R * C) // 2
        
        while low <= high:
            mid = (low + high) // 2
            count = 0
            for i in range(R):
                count += countSmallerThanMid(matrix[i], mid)
                
            if count <= req:
                low = mid + 1
            else:
                high = mid - 1
                
        return low
