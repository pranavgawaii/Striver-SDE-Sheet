class Solution:
    def prevSmaller(self, A: list[int]) -> list[int]:
        stack = []
        result = []
        
        for num in A:
            while stack and stack[-1] >= num:
                stack.pop()
                
            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1])
                
            stack.append(num)
            
        return result
