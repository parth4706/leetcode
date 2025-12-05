class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        Sum = 0
        for i in str(n):
            mul *= int(i)
            Sum += int(i)
        return mul - Sum

