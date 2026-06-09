class Solution:
    def maxLen(self, arr: list[int], k: int) -> int:
        prefix_sums = {}
        current_sum = 0
        max_len = 0
        for i, num in enumerate(arr):
            current_sum += num
            if current_sum == k:
                max_len = i + 1
            diff = current_sum - k
            if diff in prefix_sums:
                max_len = max(max_len, i - prefix_sums[diff])
            if current_sum not in prefix_sums:
                prefix_sums[current_sum] = i
        return max_len
