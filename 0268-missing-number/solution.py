class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        m = min(nums)
        if 0 not in nums:
            return 0
        for i in range(len(nums)):
            if (m + i) not in nums:
                return m+i
        return m + i +1
