class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        n = len(nums)
        for j in range(n-1):
            for i in range(len(nums)-1-c):
                nums[i] = nums[i] + nums[i+1]
                nums[i]%= 10
            c +=1
        return nums[0]
