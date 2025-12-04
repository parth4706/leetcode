class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] > nums[2] and nums[0] + nums[2] > nums[1] and nums[2] + nums[1] > nums[0]:
            if nums[0]== nums[1]:
                if nums[1]==nums[2]:
                    return "equilateral"
                else:
                    return "isosceles"
            elif nums[1] == nums[2]:
                return "isosceles"
            else:
                return "scalene"
        else:
            return "none"
