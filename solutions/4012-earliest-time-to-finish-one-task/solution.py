class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(i+j for i,j in tasks)
