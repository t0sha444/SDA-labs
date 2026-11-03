from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        buffer = [0] * len(nums)

        def merge_sort(left: int, right: int) -> None:
            if left >= right:
                return

            middle = (left + right) // 2
            merge_sort(left, middle)
            merge_sort(middle + 1, right)

            i = left
            j = middle + 1
            k = left

            while i <= middle and j <= right:
                if nums[i] <= nums[j]:
                    buffer[k] = nums[i]
                    i += 1
                else:
                    buffer[k] = nums[j]
                    j += 1
                k += 1

            while i <= middle:
                buffer[k] = nums[i]
                i += 1
                k += 1

            while j <= right:
                buffer[k] = nums[j]
                j += 1
                k += 1

            for position in range(left, right + 1):
                nums[position] = buffer[position]

        merge_sort(0, len(nums) - 1)
        return nums
