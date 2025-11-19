class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        n = str(n)
        while int(n) != 1:
            Sum = 0
            for i in n:
                Sum += int(i)**2
            if Sum == 1:
                break
            if Sum in seen:
                return False
            n = str(Sum)
            seen.add(Sum)
        return True

