class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        for i in range(t):
            r = n+i
            mul = 1
            for j in str(r):
                mul *= int(j)
            if mul%t == 0:
                return r

