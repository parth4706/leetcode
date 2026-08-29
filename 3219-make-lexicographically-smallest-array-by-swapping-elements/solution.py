class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        arr = sorted((nums[i], i) for i in range(len(nums)))
        ans = nums[:]

        def solve(start):
            if start >= len(arr):
                return

            end = start

            while end + 1 < len(arr) and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            values = sorted(arr[i][0] for i in range(start, end + 1))
            indices = sorted(arr[i][1] for i in range(start, end + 1))

            for i in range(len(values)):
                ans[indices[i]] = values[i]

            solve(end + 1)

        solve(0)
        return ans
