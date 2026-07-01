class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = "".join(sorted(s1))
        n = len(k)
        for i in range(len(s2)-n+1):
            w= "".join(sorted(s2[i:i+n]))
            if k in w:
                return True 
        return False
