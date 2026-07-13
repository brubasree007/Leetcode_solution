class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        ans=[]
        for key in freq:
            if freq[key]>len(nums)//3:
                ans.append(key)
        return ans
