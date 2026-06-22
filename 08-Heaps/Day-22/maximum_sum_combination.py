import heapq

class Solution:
    def solve(self, A: list[int], B: list[int], C: int) -> list[int]:
        A.sort(reverse=True)
        B.sort(reverse=True)
        
        max_heap = []
        heapq.heappush(max_heap, (-(A[0] + B[0]), 0, 0))
        
        visited = set()
        visited.add((0, 0))
        
        result = []
        
        for _ in range(C):
            current_sum, i, j = heapq.heappop(max_heap)
            result.append(-current_sum)
            
            if i + 1 < len(A) and (i + 1, j) not in visited:
                heapq.heappush(max_heap, (-(A[i + 1] + B[j]), i + 1, j))
                visited.add((i + 1, j))
                
            if j + 1 < len(B) and (i, j + 1) not in visited:
                heapq.heappush(max_heap, (-(A[i] + B[j + 1]), i, j + 1))
                visited.add((i, j + 1))
                
        return result
