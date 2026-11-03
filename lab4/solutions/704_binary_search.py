from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        return -1
