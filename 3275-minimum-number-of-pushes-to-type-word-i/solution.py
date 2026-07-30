from collections import Counter
class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        a = len(word)
        res = 0
        i = 1
        while a > 0:
            if a >=8:
                res += 8*i
                i += 1
                a -= 8
            else:
                res += a*i
                a = 0
        return res

