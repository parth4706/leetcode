class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        power = 1000

        while power <= n:
            res += n - power + 1
            power *= 1000

        return res
