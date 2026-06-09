class Solution:
    def findRepeatingAndMissing(self, nums: list[int]) -> list[int]:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        expected_sum_sq = n * (n + 1) * (2 * n + 1) // 6
        
        actual_sum = sum(nums)
        actual_sum_sq = sum(x * x for x in nums)
        
        diff_sum = actual_sum - expected_sum
        diff_sum_sq = actual_sum_sq - expected_sum_sq
        
        sum_xy = diff_sum_sq // diff_sum
        
        repeating = (diff_sum + sum_xy) // 2
        missing = sum_xy - repeating
        
        return [repeating, missing]
