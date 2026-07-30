class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [float('inf'),float('-inf')]
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]== target:
                res[0] = min(res[0],m)
                r = m-1
            elif nums[m] > target:
                r = m-1
            else:
                l = m+1
        if res[0] == float('inf'):
            res[0] = -1
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]== target:
                res[1] = max(res[1],m)
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                l = m+1
        if res[1] == float('-inf'):
            res[1] = -1

        return res
