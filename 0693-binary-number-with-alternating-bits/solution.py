class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        k = str(bin(n))
        for i in range(len(k)-1):
            if k[i] == k[i+1]:
                return False
        return True
        
