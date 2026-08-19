import math
class Solution(object):
    def smallestAbsent(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        avg = sum(nums)/len(nums)
        s = set(nums)
        for i in range(int(avg)+1,max(nums)+2):
            if i not in s and i > 0:
                return i
        return 1
