class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi=max(candies)
        m=[]
        for i in candies:
            if i+extraCandies>=maxi:
                m.append(True)
            else:
                m.append(False)
        return m

