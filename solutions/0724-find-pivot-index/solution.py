class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            l=sum(nums[:i])
            r=sum(nums[i+1:])
            if l==r:
                return i
        return -1
