class Solution(object):
    def stoneGameIX(self, stones):
        s1 = 0
        s2 = 0
        s3 = 0

        for x in stones:
            if x % 3 == 0:
                s3 += 1
            elif x % 3 == 1:
                s1 += 1
            else:
                s2 += 1

        if s3 % 2 == 0:
            return s1 > 0 and s2 > 0
        else:
            return abs(s1 - s2) > 2
