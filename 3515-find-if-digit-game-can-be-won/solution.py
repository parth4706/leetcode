class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        S1 =0
        S2 = 0
        for i in nums:
            if i > 9:
                S2 += i
            else:
                S1 += i
        return S2 != S1
