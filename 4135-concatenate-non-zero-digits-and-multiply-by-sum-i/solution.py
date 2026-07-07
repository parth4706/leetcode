class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==0:
            return 0
        s = str(n).replace("0","")
        c = 0
        for i in s:
            c += int(i)
        return c*(int(s))
