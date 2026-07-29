class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort()
        while len(stones) > 1:
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            else:
                k = stones.pop()
                stones[-1] = abs(stones[-1] - k)
                stones.sort()
        if stones:
            return stones[0]    
        return 0
