class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        seen = set()
        right = len(nums)
        count = 0
        while left < right and count < len(nums) / 2 +1:
            m = (left + right)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                left = m
            else:
                right = m
            count += 1            
        
        return -1

