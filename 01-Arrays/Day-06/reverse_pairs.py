class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def merge_and_count(left, mid, right):
            count = 0
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - (mid + 1))
            
            temp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= right:
                temp.append(nums[j])
                j += 1
                
            for loop_idx, val in enumerate(temp):
                nums[left + loop_idx] = val
            return count

        def merge_sort_and_count(left, right):
            if left >= right:
                return 0
            mid = (left + right) // 2
            count = merge_sort_and_count(left, mid)
            count += merge_sort_and_count(mid + 1, right)
            count += merge_and_count(left, mid, right)
            return count

        return merge_sort_and_count(0, len(nums) - 1)
