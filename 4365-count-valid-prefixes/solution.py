class Solution(object):
    def countValidPrefixes(self, s):
        """
        :type s: str
        :rtype: int
        """
        z = 0
        o = 0
        res = 0
        for i in s:
            if i == "1":
                o +=1
            else:
                z += 1
            if abs(o-z) <=1:
                res += 1
        return res
