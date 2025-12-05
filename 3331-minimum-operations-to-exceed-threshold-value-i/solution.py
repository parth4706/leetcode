class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        while nums:
            if nums[-1] >= k:
                return n - len(nums)
            nums.pop()
