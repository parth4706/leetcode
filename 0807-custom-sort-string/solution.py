class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        r = ""
        for i in order:
            k = s.count(i)
            if s != 0:
                r = r + (i * k)
        l = [x for x in s if x not in order]
        return r + "".join(l)
