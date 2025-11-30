class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        left = 0 
        right = 0
        while left < len(s) and right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            w = right - left +1
            max_len = max(w,max_len)
            seen.add(s[right])
            right += 1
        return max_len

