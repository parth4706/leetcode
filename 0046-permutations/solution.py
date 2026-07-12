class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        k = []
        seen = set()
        def f(idx):
            if idx == len(nums):
                res.append(k[:])
                return
            for i in range(len(nums)):
                if nums[i] in seen:
                    continue
                else:
                    seen.add(nums[i])
                    k.append(nums[i])
                    f(idx+1)
                    k.pop()
                    seen.remove(nums[i])
        f(0)
        return res
            
