class Solution:
    def NthRoot(self, n: int, m: int) -> int:
        low = 1
        high = m
        
        while low <= high:
            mid = (low + high) // 2
            val = mid ** n
            
            if val == m:
                return mid
            elif val < m:
                low = mid + 1
            else:
                high = mid - 1
                
        return -1
