class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = 0

        for i in range(n):
            for j in range(i, n):
                s = prefix[j + 1] - prefix[i]

                if s % 10 != x:
                    continue

                first = int(str(s)[0])

                if first == x:
                    ans += 1

        return ans
