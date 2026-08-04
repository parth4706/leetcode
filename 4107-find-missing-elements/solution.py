class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mi = min(nums)
        ma = max(nums)
        s = set(nums)
        res = []
        for i in range(mi,ma+1):
            if i not in s:
                res.append(i)
        return res
            
