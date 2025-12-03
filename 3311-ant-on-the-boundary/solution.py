class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        curr, cnt = 0, 0
        for x in nums:
            curr += x
            if curr == 0:
                cnt += 1
        return cnt
