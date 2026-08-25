class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = 1
        nums = set(nums)
        while True:
            if (i*k) not in nums:
                return i*k
            else:
                i+= 1

