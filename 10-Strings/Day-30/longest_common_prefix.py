class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
            
        shortest_str = min(strs, key=len)
        
        for i, char in enumerate(shortest_str):
            for other_str in strs:
                if other_str[i] != char:
                    return shortest_str[:i]
                    
        return shortest_str
