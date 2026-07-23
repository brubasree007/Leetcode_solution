class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=one=two=0
        for i in nums:
            if i==0:
                zero+=1
            elif i==1:
                one+=1
            else:
                two+=1
        index=0
        while zero:
            nums[index]=0
            index+=1
            zero-=1
        
        while one:
            nums[index]=1
            index+=1
            one-=1
        while two:
            nums[index]=2
            index+=1
            two-=1
        
