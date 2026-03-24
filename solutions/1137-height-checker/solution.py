class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ex=sorted(heights)
        a=0
        for i in range(len(heights)):
            if ex[i]!=heights[i]:
                a+=1
        return a

