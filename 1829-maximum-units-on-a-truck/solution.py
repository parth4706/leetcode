class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        res = 0
        boxTypes.sort(key=lambda x: x[1],reverse = True)
        for i in boxTypes:
            if truckSize == 0:
                return res
            res += min(truckSize,i[0])*i[1]
            truckSize -= min(truckSize,i[0])
        return res
