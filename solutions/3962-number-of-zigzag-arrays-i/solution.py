class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1

        up = [0] * m
        down = [0] * m

        # length 2 initialization
        for x in range(m):
            up[x] = x
            down[x] = m - 1 - x

        for _ in range(3, n + 1):

            pref_down = [0] * (m + 1)
            pref_up = [0] * (m + 1)

            for i in range(m):
                pref_down[i + 1] = (pref_down[i] + down[i]) % MOD
                pref_up[i + 1] = (pref_up[i] + up[i]) % MOD

            total_up = pref_up[m]

            new_up = [0] * m
            new_down = [0] * m

            for x in range(m):
                # previous value < x
                new_up[x] = pref_down[x]

                # previous value > x
                new_down[x] = (total_up - pref_up[x + 1]) % MOD

            up = new_up
            down = new_down

        ans = (sum(up) + sum(down)) % MOD
        return ans
