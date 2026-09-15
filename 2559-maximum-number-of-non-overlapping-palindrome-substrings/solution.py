class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        for i in range(n):
            dp[i + 1] = max(dp[i + 1], dp[i])

            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 >= k:
                    dp[right + 1] = max(dp[right + 1], dp[left] + 1)
                left -= 1
                right += 1

            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 >= k:
                    dp[right + 1] = max(dp[right + 1], dp[left] + 1)
                left -= 1
                right += 1

        return dp[n]
