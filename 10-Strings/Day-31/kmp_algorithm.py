class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
            
        m = len(needle)
        lps = [0] * m
        
        prev_lps = 0
        i = 1
        
        while i < m:
            if needle[i] == needle[prev_lps]:
                lps[i] = prev_lps + 1
                prev_lps += 1
                i += 1
            elif prev_lps == 0:
                lps[i] = 0
                i += 1
            else:
                prev_lps = lps[prev_lps - 1]
                
        n = len(haystack)
        i = 0
        j = 0
        
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                
            if j == m:
                return i - m
                
            elif i < n and haystack[i] != needle[j]:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
                    
        return -1
