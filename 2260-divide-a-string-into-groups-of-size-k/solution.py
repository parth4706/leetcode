class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        l = len(s)
        x = l%k
        if x:
            s = s +fill*(k-x)
        res = []
        for i in range(len(s)//k):
            w = s[k*i:k*i+k]
            res.append(w)
        return res
