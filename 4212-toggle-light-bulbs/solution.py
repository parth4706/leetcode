from collections import Counter
class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        res = []
        c = Counter(bulbs)
        for i in c:
            if c[i]%2==1:
                res.append(i)
        return sorted(list(set(res)))
