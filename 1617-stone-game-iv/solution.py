class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo = {}

        def dfs(x):
            if x == 0:
                return False

            if x in memo:
                return memo[x]

            j = 1
            while j * j <= x:
                if not dfs(x - j * j):
                    memo[x] = True
                    return True
                j += 1

            memo[x] = False
            return False

        return dfs(n)
        
