class Solution(object):
    def buildArray(self, nums):
        return [nums[nums[i]] for i in range(0,len(nums))]
