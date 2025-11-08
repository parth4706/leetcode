class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) -1
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort(key=lambda x: x[0])
        while left < right:
            if arr[left][0] + arr[right][0] == target:
                return arr[left][1],arr[right][1]
            elif arr[left][0] + arr[right][0] > target:
                right -= 1
            elif arr[left][0] + arr[right][0] < target:
                left += 1
