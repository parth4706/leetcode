class Solution(object):
    def checkRecord(self, n):
        MOD = 10**9 + 7

        memo = [[[-1] * 3 for _ in range(2)] for _ in range(n)]

        def f(i, a, l):
            if i == n:
                return 1
            if memo[i][a][l] != -1:
                return memo[i][a][l]
            res = 0
            res = f(i + 1, a, 0)
            if a == 0:
                res = (res + f(i + 1, 1, 0)) % MOD
            if l < 2:
                res = (res + f(i + 1, a, l + 1)) % MOD
            memo[i][a][l] = res
            return res
        return f(0, 0, 0)
