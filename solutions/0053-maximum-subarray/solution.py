class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=0
        maxi=nums[0]
        
        for i in nums:
            curr+=i
            if curr>maxi:
                maxi=curr
            if curr<0:
                curr=0
        return maxi
