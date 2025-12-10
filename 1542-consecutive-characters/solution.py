class Solution:
    def maxPower(self, s: str) -> int:
        res =1
        s +=" "
        for i in range(len(s)-1):
            l = i+1
            Count = 1
            while s[i] == s[l] and l < len(s)-1:
                l +=1
                Count +=1
            res = max(res,Count)
        return res
