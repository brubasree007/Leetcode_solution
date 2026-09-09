class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums=sorted(nums)
        sq=[]
        for i in nums:
            sq.append(i*i)
        return sorted(sq)
