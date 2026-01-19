class Solution:
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])

        # Step 1: Create prefix sum matrix
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (
                    mat[i-1][j-1]
                    + prefix[i-1][j]
                    + prefix[i][j-1]
                    - prefix[i-1][j-1]
                )

        # Step 2: Try all possible square sizes
        ans = 0
        for size in range(1, min(m, n) + 1):
            found = False
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    square_sum = (
                        prefix[i+size][j+size]
                        - prefix[i][j+size]
                        - prefix[i+size][j]
                        + prefix[i][j]
                    )
                    if square_sum <= threshold:
                        found = True
                        break
                if found:
                    break

            if found:
                ans = size
            else:
                break

        return ans

