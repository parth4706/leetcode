class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(bin(num))[2:]
        k = int("1"*len(num))
        return int(str(k - int(num)),2)

        
