class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        k = sorted(list(set(nums)))
        if len(k) < 3:
            return max(k)
        return k[-3]
