class Solution(object):
    def maxAscendingSum(self, nums):
        i = 0
        n = len(nums)
        m = 0

        while i < n:
            s = nums[i]

            while i < n - 1 and nums[i] < nums[i + 1]:
                i += 1
                s += nums[i]

            m = max(m, s)
            i += 1

        return m
