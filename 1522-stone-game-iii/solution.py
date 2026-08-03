class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        memo = {}
        def f(i):
            if i in memo:
                return memo[i]
            if i >= len(stoneValue):
                return 0
            one = stoneValue[i] - f(i+1)
            if i  < len(stoneValue)-1:
                two = stoneValue[i]+stoneValue[i+1]-f(i+2)
            else:
                two = one
            if i +1 < len(stoneValue)-1:
                three = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - f(i+3)
            else:
                three = two
            memo[i] = max(one,two,three)
            return memo[i]
        if f(0) > 0:
            return "Alice"
        elif f(0) < 0:
            return "Bob"
        return "Tie"

