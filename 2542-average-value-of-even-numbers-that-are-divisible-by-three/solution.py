class Solution:
    def averageValue(self, nums: List[int]) -> int:
        Count = 0
        Sum = 0
        for i in nums:
            if i%6==0:
                Sum +=i
                Count += 1
        if Count ==0:
            return 0
        return Sum//Count
