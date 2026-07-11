class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        prefix = 0
        res = 0
        for i in range(len(gas)):
            prefix += gas[i] - cost[i]
            if prefix <0:
                prefix = 0
                res = i+1
        return res
        

