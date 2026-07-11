class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        m = -1
        for i in accounts:
            m = max(m,sum(i))
        return m
