class Solution:
    def reverseVowels(self, s: str) -> str:
        vow="aeiouAEIOU"
        v=[]
        for i in s:
            if i in vow:
                v.append(i)
        res=''
        v=v[::-1]
        for i in s:
            if i in vow:
                res+=v.pop(0)
            else:
                res+=i
        return res 
