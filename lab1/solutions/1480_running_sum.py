from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        total = 0

        for number in nums:
            total += number
            result.append(total)

        return result
