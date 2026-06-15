class Solution:
    def minimumPlatform(self, n: int, arr: list[int], dep: list[int]) -> int:
        arr.sort()
        dep.sort()
        
        plat_needed = 1
        result = 1
        i = 1
        j = 0
        
        while i < n and j < n:
            if arr[i] <= dep[j]:
                plat_needed += 1
                i += 1
            else:
                plat_needed -= 1
                j += 1
            
            result = max(result, plat_needed)
            
        return result
