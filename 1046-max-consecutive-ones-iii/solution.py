class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_w = 0
        num_0 = 0
        n = len(nums)
        l = 0
        for i in range(n):
            if nums[i] == 0:
                num_0 += 1
            
            while num_0 > k:
                if nums[l] == 0:
                    num_0 -= 1
                l+=1
            w = i-l +1
            max_w = max(w,max_w)
        return max_w
