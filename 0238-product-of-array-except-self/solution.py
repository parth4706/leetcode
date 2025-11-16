class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        p_z = 1
        rez = []
        if nums.count(0) > 1:
            return [0]*len(nums)
        for i in range(len(nums)):
            p_z *= nums[i]
            if nums[i] != 0:
                p*= nums[i]
        for x in nums:
            if x != 0:
                rez.append(p_z//x)
            else:
                rez.append(p)
        return rez
