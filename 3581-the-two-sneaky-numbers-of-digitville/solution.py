class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        k =[]
        for i in range(len(nums)):
            if nums.count(nums[i]) > 1:
                k.append(nums[i])
        return list(set(k))
