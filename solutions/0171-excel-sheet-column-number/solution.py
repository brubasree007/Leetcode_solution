class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res=0
        for ch in columnTitle:
            v=ord(ch)-ord("A")+1
            res=res*26+v
        return res
