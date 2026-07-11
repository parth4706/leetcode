class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        s = 0
        m = 0
        for i in gain:
            s += i
            m = max(m,s)
        return m
