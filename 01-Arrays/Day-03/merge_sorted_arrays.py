class Solution:
    def merge(self, arr1: list[int], arr2: list[int]) -> None:
        n, m = len(arr1), len(arr2)
        i = n - 1
        j = 0
        while i >= 0 and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
                i -= 1
                j += 1
            else:
                break
        arr1.sort()
        arr2.sort()
