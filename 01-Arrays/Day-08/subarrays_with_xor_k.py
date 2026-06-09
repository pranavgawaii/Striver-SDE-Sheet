class Solution:
    def solve(self, A: list[int], B: int) -> int:
        prefix_xor = {0: 1}
        current_xor = 0
        count = 0
        for num in A:
            current_xor ^= num
            target = current_xor ^ B
            if target in prefix_xor:
                count += prefix_xor[target]
            prefix_xor[current_xor] = prefix_xor.get(current_xor, 0) + 1
        return count
