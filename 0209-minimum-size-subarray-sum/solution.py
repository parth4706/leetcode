class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        curr_sum = 0
        flag = 0
        res = float("inf")
        for i in range(len(nums)):
            curr_sum += nums[i]
            
            while curr_sum >= target :
                res = min(res, i - l + 1)
                curr_sum -= nums[l]
                l += 1
        if res == float("inf"):
            return 0
        else:
            return res

