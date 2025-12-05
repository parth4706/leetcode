class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if nums[i] > 0:
                break
            l = i+1
            r = n-1
            if nums[r] < 0:
                break
            while l <r:
                if nums[l] + nums[r] + nums[i] == 0 and (nums[i],nums[l],nums[r]) not in seen:
                    res.append([nums[i],nums[l],nums[r]])
                    seen.add((nums[i],nums[l],nums[r]))
                    l+=1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                else:
                    l +=1
        return res
        
