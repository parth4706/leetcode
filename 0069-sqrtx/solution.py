class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <=1:
            return x

        r = x//2
        l = 0
        while l <= r:
            m = l + (r-l)//2
            if m*m == x:
                return m
            elif m *m >x:
                r = m -1
            else:
                l = m+1
        return l-1
