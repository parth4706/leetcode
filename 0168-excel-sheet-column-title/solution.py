class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        res = []
        num = columnNumber
        while num > 0:
            res.append(capitals[(num-1)%26])
            num = (num-1) // 26
        res.reverse()
        return ''.join(res)
