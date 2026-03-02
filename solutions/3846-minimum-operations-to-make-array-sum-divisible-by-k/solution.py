class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        tot=sum(nums)
        rem=tot%k
        return rem
