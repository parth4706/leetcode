class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {}

        def f(i, s):
            if (i, s) in memo:
                return memo[(i, s)]

            if i == len(nums):
                return 1 if s == target else 0

            plus = f(i + 1, s + nums[i])
            minus = f(i + 1, s - nums[i])

            memo[(i, s)] = plus + minus
            return memo[(i, s)]

        return f(0, 0)
