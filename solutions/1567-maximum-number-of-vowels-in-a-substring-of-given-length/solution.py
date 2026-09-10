class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow="aeiou"
        arr=s[:k]
        count=0
        for i in range(k):
            if s[i] in vow:
                count+=1
        max=count
        for i in range(k,len(s)):
            if arr[0] in vow:
                count-=1
            if s[i] in vow:
                count+=1
            arr=arr[1:]+s[i]
            if max<count:
                max=count
        return max 
