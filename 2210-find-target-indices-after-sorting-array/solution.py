class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            nums.sort()
            s = nums.index(target)
            lst = [s]
            while s<len(nums)-1 and nums[s]==nums[s+1]:
                lst.append(s+1)
                s += 1
            return lst
        return []
