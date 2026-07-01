class Solution:
    def search(self, text: str, pattern: str) -> list[int]:
        s = pattern + "$" + text
        n = len(s)
        z = [0] * n
        l = 0
        r = 0
        
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
                
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
                
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1
                
        res = []
        p_len = len(pattern)
        
        for i in range(p_len + 1, n):
            if z[i] == p_len:
                res.append(i - p_len - 1)
                
        return res
