class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        base=0
        pair={}
        maxi=0
        for i in range(len(nums)-1):
            a,b=nums[i],nums[i+1]
            if a==b:
                base+=1
            else:
                unorder=(min(a,b),max(a,b))
                pair[unorder]=pair.get(unorder,0)+1
                if pair[unorder]>maxi:
                    maxi=pair[unorder]
        return base+maxi
