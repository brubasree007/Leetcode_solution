class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        al=0
        hi=[0]
        for i in gain:
            al+=i
            hi.append(al)
        return max(hi)
