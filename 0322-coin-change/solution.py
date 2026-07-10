class Solution(object):
    def coinChange(self, coins, amount):
        seen = {}
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

        res = dfs(amount)
        return -1 if res == float('inf') else res
