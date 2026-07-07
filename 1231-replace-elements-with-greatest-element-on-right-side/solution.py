class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        r = len(arr)  - 1
        m = -1
        while r >= 0:
            temp = arr[r]
            arr[r] = m
            if temp > m:
                m = temp
            r -= 1
        return arr
