class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        next_greater = {}
        
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
                
            if stack:
                next_greater[num] = stack[-1]
            else:
                next_greater[num] = -1
                
            stack.append(num)
            
        return [next_greater.get(num, -1) for num in nums1]
