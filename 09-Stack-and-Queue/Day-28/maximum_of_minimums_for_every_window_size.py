class Solution:
    def maxOfMin(self, arr: list[int], n: int) -> list[int]:
        left = [-1] * n
        right = [n] * n
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
            
        stack.clear()
        
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
            
        ans = [0] * (n + 1)
        
        for i in range(n):
            length = right[i] - left[i] - 1
            ans[length] = max(ans[length], arr[i])
            
        for i in range(n - 1, 0, -1):
            ans[i] = max(ans[i], ans[i + 1])
            
        return ans[1:]
