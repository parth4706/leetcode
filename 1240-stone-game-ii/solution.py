class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = {}

        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]

        def f(i, m):
            if i >= n:
                return 0

            if (i, m) in memo:
                return memo[(i, m)]

            ans = 0

            for j in range(1, 2 * m + 1):
                if i + j > n:
                    break

                opponent = f(i + j, max(m, j))

                ans = max(ans, suffix[i] - opponent)

            memo[(i, m)] = ans
            return ans

        return f(0, 1)
