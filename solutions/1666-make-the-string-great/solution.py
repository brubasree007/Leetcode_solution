class Solution:
    def makeGood(self, s: str) -> str:
        arr=[]
        for i in s:
            if arr and abs(ord(arr[-1]) - ord(i))==32:
                arr.pop()
            else:
                arr.append(i)
        return "".join(arr)

