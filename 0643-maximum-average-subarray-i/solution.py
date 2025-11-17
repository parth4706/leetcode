class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        S = sum(nums[:k])
        max_S = S
        if len(nums) == k:
            return sum(nums) / k
        for i in range(k,len(nums)):
            S += nums[i] - nums[i-k]
            max_S = max(max_S,S)
            
        return max_S / k
