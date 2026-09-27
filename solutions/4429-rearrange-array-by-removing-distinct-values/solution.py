class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans=[]
        while nums:
            dis=sorted(list(set(nums)))
            ans.extend(dis)
            for val in dis:
                nums.remove(val)
        return ans
