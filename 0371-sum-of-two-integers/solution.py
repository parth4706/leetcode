class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """



        mask = 0xFFFFFFFF
        a = a & mask
        b = b & mask

        while b:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        if a >> 31:
            return ~(a ^ mask)

        return a
