class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        x = 0
        for i in nums:
            x ^= i
        
        if x != 0 :
            return len(nums)
        else:
            if len(s) > 1:
                return len(nums)-1
            else:
                if 0 in s:
                    return 0
                else:
                    return len(nums)-1
