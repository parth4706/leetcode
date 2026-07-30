class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        res = [-1]
        def f(l,r):
            m = (l + r)//2
            if l>r:
                return
            if nums[m] == target:
                res[0] = m
                return 
            elif nums[m]> target:
                f(l,m-1)
            else:
                f(m+1,r)
        f(l,r)  
        return res[0]
                
