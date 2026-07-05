class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = 0
        for n in nums:
            if res < 0:
                return False
            elif n > res:
                res = n
            res -= 1
            
        return True

