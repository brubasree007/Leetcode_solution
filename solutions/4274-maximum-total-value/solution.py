class Solution:
    def maxTotalValue(self, value: list[int], decay: list[int], m: int) -> int:
        MOD = 10**9 + 7

        def count_ge(x):
            cnt = 0
            for v, d in zip(value, decay):
                if v >= x:
                    cnt += (v - x) // d + 1
            return cnt

        lo, hi = 1, max(value)

        while lo <= hi:
            mid = (lo + hi) // 2

            if count_ge(mid) >= m:
                lo = mid + 1
            else:
                hi = mid - 1

        T = hi

        total = 0
        taken = 0

        for v, d in zip(value, decay):
            if v > T:
                cnt = (v - (T + 1)) // d + 1

                taken += cnt

                last = v - (cnt - 1) * d

                total += cnt * (v + last) // 2

        total += (m - taken) * T

        return total % MOD
