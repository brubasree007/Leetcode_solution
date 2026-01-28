class Solution:
    def isValid(self, s: str) -> bool:
        l={'(':')','{':'}','[':']'}
        stk=[]
        for i in s:
            if i in l:
                stk.append(i)
            else:
                if(not stk or l[stk.pop()]!=i):
                    return False
        return not stk
