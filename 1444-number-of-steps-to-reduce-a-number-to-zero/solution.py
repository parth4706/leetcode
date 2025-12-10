class Solution:
    def numberOfSteps(self, num: int) -> int:
        Count =0
        while True:
            if num ==0:
                return Count
            elif num%2==0:
                num = num//2
            else:
                num -= 1
            Count +=1
        

