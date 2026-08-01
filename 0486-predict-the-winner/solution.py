class Solution(object):
    def predictTheWinner(self, nums):
        n = len(nums)

        memo = {}

        def f(l, r):
            if l == r:
                return nums[l]
            if (l, r) in memo:
                return memo[(l, r)]
            left = nums[l] - f(l + 1, r)
            right = nums[r] - f(l, r - 1)
            memo[(l, r)] = max(left, right)

            return memo[(l, r)]

        return f(0, n - 1) >= 0
