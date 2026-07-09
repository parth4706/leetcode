class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        seen = {}
        def f(i):
            if i in seen:
                return seen[i]
            if i == 0 or i == 1:
                return 0
            seen[i] = min(
                cost[i-1] + f(i-1),
                cost[i-2] + f(i-2)

                )
            return seen[i]
        n = len(cost)
        return f(n)
