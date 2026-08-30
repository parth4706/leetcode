class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ma = nums.index(max(nums))+1
        mi = nums.index(min(nums))+1
        res = min([max(ma,mi),len(nums)-min(ma,mi)+1,min(ma,mi)+len(nums)-max(ma,mi)+1])
        return res

