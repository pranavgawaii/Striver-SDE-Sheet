class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w

class Solution:
    def fractionalknapsack(self, W, arr, n):
        arr.sort(key=lambda x: x.value / x.weight, reverse=True)
        
        total_value = 0.0
        
        for item in arr:
            if item.weight <= W:
                W -= item.weight
                total_value += item.value
            else:
                total_value += item.value * (W / item.weight)
                break
                
        return total_value
