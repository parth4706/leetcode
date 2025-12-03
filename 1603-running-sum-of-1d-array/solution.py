class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        Sum = 0
        for i in nums:
            Sum += i
            res.append(Sum)
        return res
