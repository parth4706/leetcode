class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        k = arr[0] - arr[1]
        for i in range(len(arr)-1):
            if (arr[i] - arr[i+1]) != k:
                return False
        return True
