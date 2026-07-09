class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = len(nums) - 1
        seen = {}
        if i < 2:
            return max(nums)
        def f(i):
            if i in seen:
                return seen[i]
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0],nums[1])
            seen[i] = max((nums[i] + f(i-2)),f(i-1))
            return seen[i]
        seen2 = {}
        def f2(i):
            if i in seen2:
                return seen2[i]
            if i == 1:
                return nums[1]
            if i == 2:
                return max(nums[1],nums[2])
            seen2[i] = max((nums[i] + f2(i-2)),f2(i-1))
            return seen2[i]
        
        return max(f(i-1),f2(i))
        
