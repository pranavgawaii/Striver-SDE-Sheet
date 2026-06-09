class Solution:
    def countInversions(self, arr: list[int]) -> int:
        def merge_and_count(temp_arr, left, mid, right):
            inv_count = 0
            i = left
            j = mid + 1
            k = left
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp_arr[k] = arr[i]
                    i += 1
                else:
                    temp_arr[k] = arr[j]
                    inv_count += (mid - i + 1)
                    j += 1
                k += 1
            while i <= mid:
                temp_arr[k] = arr[i]
                i += 1
                k += 1
            while j <= right:
                temp_arr[k] = arr[j]
                j += 1
                k += 1
            for loop_idx in range(left, right + 1):
                arr[loop_idx] = temp_arr[loop_idx]
            return inv_count

        def merge_sort_and_count(temp_arr, left, right):
            inv_count = 0
            if left < right:
                mid = (left + right) // 2
                inv_count += merge_sort_and_count(temp_arr, left, mid)
                inv_count += merge_sort_and_count(temp_arr, mid + 1, right)
                inv_count += merge_and_count(temp_arr, left, mid, right)
            return inv_count

        temp = [0] * len(arr)
        return merge_sort_and_count(temp, 0, len(arr) - 1)
