class Solution:
    def subsetSums(self, arr: list[int], n: int) -> list[int]:
        result = []
        
        def solve(index, current_sum):
            if index == n:
                result.append(current_sum)
                return
            solve(index + 1, current_sum + arr[index])
            solve(index + 1, current_sum)
            
        solve(0, 0)
        return sorted(result)
