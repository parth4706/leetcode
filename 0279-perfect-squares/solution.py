class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        seen = {}
        coins = set()
        i = 1
        while i**2 <= n:
            coins.add(i**2)
            i += 1
        def dfs(rem):
            if rem in seen:
                return seen[rem]
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')

            ans = float('inf')

            for coin in coins:
                ans = min(ans, 1 + dfs(rem - coin))
            seen[rem] = ans
            return ans

        res = dfs(n)
        return -1 if res == float('inf') else res
