class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        # using backtrack recursion XOR= ^
        # 0^0 = 0
        # 1^1 = 0
        # 1^0 = 1
        # 0^1 = 1
        def f(n):
            XOR = 0
            for i in n:
                XOR ^= i
            if XOR == 0:
                return True
            else:
                return False
        
        if f(nums) == True:
            return True
        elif len(nums)%2== 0:
            return True
        else:
            return False
            
        



