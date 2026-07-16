class Solution(object):
    def countElements(self, nums, k):
        if k == 0:
            return len(nums)

        nums.sort()
        n = len(nums)

        ans = 0
        for i in range(n - k):
            if nums[i] < nums[n - k]:
                ans += 1
        return ans
