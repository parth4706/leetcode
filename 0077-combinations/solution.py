class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        r = []
        def backtrack(s):
            if len(r) == k:
                res.append(r[:])
                return
            for i in range(s,n+1):
                if i not in r:
                    r.append(i)
                    backtrack(i+1)
                    r.pop()
            return
        backtrack(1)
        return res

