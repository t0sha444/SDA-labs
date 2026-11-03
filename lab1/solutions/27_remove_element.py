from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for number in nums:
            if number != val:
                nums[k] = number
                k += 1

        return k
