class Solution:
    def isHappy(self, n: int) -> bool:
        while n!=1 and n!=4:
            tot=0
            while n>0:
                dig=n%10
                tot+=dig*dig
                n//=10
            n=tot
        return n==1

