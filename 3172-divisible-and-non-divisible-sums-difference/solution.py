class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        Sum = 0
        for i in range(n+1):
            if i%m != 0:
                Sum+=i
            else:
                Sum-= i
        return Sum
