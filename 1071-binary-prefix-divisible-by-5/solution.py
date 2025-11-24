class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        s = ""
        for i in nums:
            b = str(i)
            s = s+b
            if int(s,2)%5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res
