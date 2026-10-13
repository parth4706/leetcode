class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted(x * x for x in nums)
        l, r = 0, len(nums) - 1
        score = 0

        while l < r:
            score += nums[r] - nums[l]
            l += 1
            r -= 1

        if l == r:
            score += nums[l]

        return score
