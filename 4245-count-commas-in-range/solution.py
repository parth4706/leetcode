class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1000:
            return 0
        if n == 10000:
            return 9001
        else:
            return n-999
