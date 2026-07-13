class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowsum=sum(nums[:k])
        maxi=windowsum
        for i in range(k,len(nums)):
            windowsum+=nums[i]-nums[i-k]
            if windowsum>maxi:
                maxi=windowsum
        return maxi/k
