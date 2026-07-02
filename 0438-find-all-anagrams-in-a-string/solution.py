class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        c = Counter(p)
        k = len(s)
        r = len(p)
        res = []
        for i in range(k-r+1):
            w= s[i:i+r]
            if Counter(w) == c:
                res.append(i)
        return res
