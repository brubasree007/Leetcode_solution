class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        we=0
        for i in accounts:
            s=sum(i)
            we=max(we,s)
        return we
