class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        k = len(nums[0])
        nums= set(nums)
        
        res = []
        def f(s):
            if res:
                return
            if len(s)== k:
                if s not in nums:
                    res.append(s)
                return
            f(s+"0")
            f(s+"1")
        f("")
        return res[0]
