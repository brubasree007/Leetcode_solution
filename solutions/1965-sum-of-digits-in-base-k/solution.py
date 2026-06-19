class Solution:
    def sumBase(self, n: int, k: int) -> int:
        tot=0
        while n>0:
            tot+=n%k
            n//=k
        return tot
