class Solution(object):
    def largestInteger(self, nums, k):
        c = [0] * (max(nums) + 1)

        for i in range(len(nums) - k + 1):
            for x in set(nums[i:i+k]):
                c[x] += 1

        res = -1

        for i in range(len(c)):
            if c[i] == 1:
                res = i

        return res
