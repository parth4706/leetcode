class Solution(object):
    def countHousePlacements(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 4
        if n==0:
            return 0
        a = 1
        b = 1
        for i in range(n-1):
            a,b = b,a+b
        res = a+b
        return (res**2)%(10**9+7)

