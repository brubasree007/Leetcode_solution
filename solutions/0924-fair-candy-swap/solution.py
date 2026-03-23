class Solution:
    def fairCandySwap(self, A, B):
        return next([x,x+(sum(B)-sum(A))//2] for x in A if x + (sum(B) - sum(A)) // 2 in set(B))
