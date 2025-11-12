class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k = 0
        if s=="":
            return True
        for i in range(len(t)):
            if s[k] == t[i]:
                k +=1
            if k == len(s):
                return True
        return False
