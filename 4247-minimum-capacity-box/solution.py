class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        """
        :type capacity: List[int]
        :type itemSize: int
        :rtype: int
        """
        m = float("inf")
        k = 0
        f= 0
        for i in range(len(capacity)):
            if capacity[i] == itemSize:
                return i
            if capacity[i] > itemSize and capacity[i] < m :
                m = capacity[i]
                k = i 
                f = 1
        if f==0:
            return -1
        return k
