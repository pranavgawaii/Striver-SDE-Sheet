class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        rev_s = s[::-1]
        
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if s[i - 1] == rev_s[j - 1]:
                    curr[j] = 1 + dp[j - 1]
                else:
                    curr[j] = max(dp[j], curr[j - 1])
            dp = curr
            
        lcs = dp[n]
        return n - lcs
