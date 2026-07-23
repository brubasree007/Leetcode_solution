class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=[]
        s=set(nums)
        n=len(nums)
        for i in range(1,n+1):
            if i not in s:
                l.append(i)
        return l
