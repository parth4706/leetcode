class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        seen = {}
        def f(m,n):
            if (m,n) in seen:
                return seen[(m,n)]
            if m == 1 or n == 1:
                return 1
            seen[(m,n)] = f(m-1,n)+f(m,n-1)
            return seen[(m,n)]
        
        return f(m,n)

