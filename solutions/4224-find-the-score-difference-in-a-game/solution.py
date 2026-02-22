from typing import List

class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 0
        active = 1   
        for i in range(len(nums)):   
            if nums[i] % 2 == 1:
                active = 2 if active == 1 else 1
            if i % 6 == 5:
                active = 2 if active == 1 else 1
            if active == 1:
                p1 += nums[i]
            else:
                p2 += nums[i]
        return p1 - p2
