from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        self.k = nums
        for x in nums:
            if nums.count(x) == 1:
                self.k.append(x)
