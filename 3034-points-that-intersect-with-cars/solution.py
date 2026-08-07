class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        
        r= [0 for i in range(0,101)]
        for i in nums:
            for j in range(i[0],i[1]+1):
                r[j] += 1
        c = 0
        for i in r:
            if i>=1:
                c+=1
        return c



