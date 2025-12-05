class Solution:
    def checkDivisibility(self, n: int) -> bool:
        Sum = 0
        Mul = 1
        for i in str(n):
            Sum += int(i)
            Mul *= int(i)
        if n%(Sum + Mul)==0:
            return True
        else:
            return False
