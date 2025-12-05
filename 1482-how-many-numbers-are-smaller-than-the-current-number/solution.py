class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        k = sorted(nums)
        lst= []
        for i in nums:
            lst.append(k.index(i))
        return lst
