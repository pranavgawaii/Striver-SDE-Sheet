class Solution:
    def rabinKarp(self, text: str, pattern: str) -> list[int]:
        n = len(text)
        m = len(pattern)
        
        if m == 0 or m > n:
            return []
            
        d = 256
        q = 101
        
        h = 1
        for _ in range(m - 1):
            h = (h * d) % q
            
        p = 0
        t = 0
        
        for i in range(m):
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[i])) % q
            
        result = []
        
        for i in range(n - m + 1):
            if p == t:
                match = True
                for j in range(m):
                    if text[i + j] != pattern[j]:
                        match = False
                        break
                if match:
                    result.append(i)
                    
            if i < n - m:
                t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
                if t < 0:
                    t = t + q
                    
        return result
