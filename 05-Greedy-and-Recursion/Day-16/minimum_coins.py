class Solution:
    def minCoins(self, coins: list[int], V: int) -> int:
        n = len(coins)
        count = 0
        for i in range(n - 1, -1, -1):
            while V >= coins[i]:
                V -= coins[i]
                count += 1
        return count
