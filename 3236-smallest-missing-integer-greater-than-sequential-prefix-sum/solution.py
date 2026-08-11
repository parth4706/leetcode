class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        length = 0
        res = 0
        max_len = 0
        i = 0

        if i < len(nums):
            s = 0
            length = 0

            while i < len(nums):
                s += nums[i]
                length += 1

                if length > max_len:
                    max_len = length
                    res = s

                if i == len(nums) - 1 or nums[i]+1 != nums[i + 1]:
                    break

                i += 1

            i += 1
        else:
            return -1
        nums = set(nums)
        
        while res in nums:
            res+=1
        return res
