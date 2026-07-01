class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        alphabets = [0]*26
        l = 0
        for r in range(len(s)):
            alphabets[ord(s[r])-65]+=1
            while (r-l+1) - max(alphabets) > k:
                alphabets[ord(s[l]) - 65] -= 1
                l +=1
            res = max(res,r-l+1)
        return res
