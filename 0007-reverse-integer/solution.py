class Solution:
    def reverse(self, x: int) -> int:
        if x<=-2147483648 or x>=2147483648:
            return 0
        if x<0:
            k = (int(str(abs(x))[::-1]))*(-1)
        else:
            k = int(str(abs(x))[::-1])
        if k<=-2147483648 or k>=2147483648:
            return 0
        else:
            return k
