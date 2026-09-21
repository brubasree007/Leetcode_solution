class Solution:
    def findMaxLength(self, nums):
        d = {0: -1}
        sum = 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                sum -= 1
            else:
                sum += 1
            if sum in d:
                max_len = max(max_len, i - d[sum])
            else:
                d[sum] = i
        return max_len
