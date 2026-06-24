class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        alice=0
        bob=0
        for num in nums:
            if num<10:
                alice+=num
            else:
                bob+=num
        return alice!=bob
