class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = len)
        s = ""
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if not strs[j][i] == strs[j+1][i]:
                    return s
            s = s + str(strs[0][i])
        return s
