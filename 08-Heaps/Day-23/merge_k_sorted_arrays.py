import heapq

class Solution:
    def mergeKArrays(self, arr, K):
        min_heap = []
        
        for i in range(K):
            if arr[i]:
                heapq.heappush(min_heap, (arr[i][0], i, 0))
                
        result = []
        
        while min_heap:
            val, array_idx, element_idx = heapq.heappop(min_heap)
            result.append(val)
            
            if element_idx + 1 < len(arr[array_idx]):
                heapq.heappush(min_heap, (arr[array_idx][element_idx + 1], array_idx, element_idx + 1))
                
        return result
