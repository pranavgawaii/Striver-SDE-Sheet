class Solution:
    def celebrity(self, M: list[list[int]], n: int) -> int:
        stack = list(range(n))
        
        while len(stack) > 1:
            a = stack.pop()
            b = stack.pop()
            
            if M[a][b] == 1:
                stack.append(b)
            else:
                stack.append(a)
                
        candidate = stack.pop()
        
        for i in range(n):
            if i != candidate:
                if M[candidate][i] == 1 or M[i][candidate] == 0:
                    return -1
                    
        return candidate
