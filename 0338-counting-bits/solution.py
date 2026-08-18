class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(n+1):
            c = 0
            k = i
            while k:
                k = k & (k-1)
                c += 1
            res.append(c)
        return res
