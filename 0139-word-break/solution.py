

class Solution(object):
    def wordBreak(self, s, wordDict):

        memo = {}
        def dfs(k):
            if k == len(s):
                return True
            if k in memo:
                return memo[k]
            for word in wordDict:
                if k + len(word) <= len(s) and s[k:k+len(word)] == word:
                    if dfs(k + len(word)):
                        memo[k] = True
                        return memo[k]
            memo[k] = False
            return memo[k]

        return dfs(0)
