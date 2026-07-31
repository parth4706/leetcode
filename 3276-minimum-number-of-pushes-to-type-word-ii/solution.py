from collections import Counter
class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        s = Counter(word)
        c = 0
        res = 0
        for i,a in s.most_common():
            res += a*(1 + c//8)
            c+= 1
        return res

