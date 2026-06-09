class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total_steps = m + n - 2
        down_steps = m - 1
        if down_steps > n - 1:
            down_steps = n - 1
        ans = 1
        for i in range(1, down_steps + 1):
            ans = ans * (total_steps - down_steps + i) // i
        return ans
