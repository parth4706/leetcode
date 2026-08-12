
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        c = {}
        l = 0
        r = 0 
        res = 0
        for r in range(len(nums)):
            c[nums[r]] = c.get(nums[r], 0) + 1
            while c[nums[r]] > k:
                c[nums[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res


