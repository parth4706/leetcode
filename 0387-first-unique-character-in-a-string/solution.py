class Solution:
    def firstUniqChar(self, s: str) -> int:
        k = sorted(Counter(s).items(),key = lambda x:x[1])
        if k[0][1] > 1:
            return -1
        else:
            return s.find(k[0][0])

