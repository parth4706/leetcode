from collections import Counter

class Solution(object):
    def deleteAndEarn(self, nums):
        s = Counter(nums)
        m = min(nums)
        n = max(nums)

        dp = [0] * (n + 1)

        dp[m] = m * s[m]

        if m + 1 <= n:
            dp[m + 1] = max(m * s[m], (m + 1) * s[m + 1])

        for i in range(m + 2, n + 1):
            dp[i] = max(dp[i-1], dp[i-2] + i * s[i])

        return dp[n]
