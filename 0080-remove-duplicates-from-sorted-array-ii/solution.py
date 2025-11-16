class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i <len(nums):
            if i < len(nums)-1 and nums[i]== nums[i+1]:
                if i < len(nums)-2 and nums[i+1] == nums[i+2]:
                    nums.pop(i+2)
                    i -= 1
            i +=1
