class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res=0
        for i in num1:
            res=res*10+(ord(i)-ord('0'))
        num=0
        for j in num2:
            num=num*10+(ord(j)-ord('0'))
        return str(res*num)
