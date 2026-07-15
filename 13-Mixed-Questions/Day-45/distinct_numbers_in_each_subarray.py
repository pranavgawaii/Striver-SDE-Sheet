from collections import defaultdict

class Solution:
    def dNums(self, A: list[int], B: int) -> list[int]:
        if B > len(A):
            return []
            
        freq = defaultdict(int)
        result = []
        distinct_count = 0
        
        for i in range(B):
            if freq[A[i]] == 0:
                distinct_count += 1
            freq[A[i]] += 1
            
        result.append(distinct_count)
        
        for i in range(B, len(A)):
            freq[A[i - B]] -= 1
            if freq[A[i - B]] == 0:
                distinct_count -= 1
                
            if freq[A[i]] == 0:
                distinct_count += 1
            freq[A[i]] += 1
            
            result.append(distinct_count)
            
        return result
