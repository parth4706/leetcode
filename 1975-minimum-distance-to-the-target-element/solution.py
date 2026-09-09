class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        a = float('inf')
        b = float('inf')
        if nums[start] == target:
            return 0
        res = 0
        for i in range(start,len(nums)):
            if nums[i] == target:
                a = abs(i-start)
                break
        i = start
        while i >=0:
            
            if nums[i] == target:
                b = abs(i-start)
                break
            i-=1
        return min(a,b)
