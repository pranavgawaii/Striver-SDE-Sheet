class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        
        def backtrack(index, current_combination, current_target):
            if current_target == 0:
                result.append(list(current_combination))
                return
            if current_target < 0 or index == len(candidates):
                return
                
            current_combination.append(candidates[index])
            backtrack(index, current_combination, current_target - candidates[index])
            
            current_combination.pop()
            backtrack(index + 1, current_combination, current_target)
            
        backtrack(0, [], target)
        return result
