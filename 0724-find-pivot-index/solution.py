class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        s = sum(nums[1:])
        if s == 0:
            return 0
        else:
            s -= nums[1]
        k = nums[0]
        if n <= 2:
            return -1
        for i in range(1,n-1):
            if s == k:
                return i
            k += nums[i]
            s -= nums[i+1]
        if k == 0:
            return n-1
        return -1
