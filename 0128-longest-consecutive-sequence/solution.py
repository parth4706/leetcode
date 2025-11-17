class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = sorted(list(set(nums)))
        i = 0
        max_count =0
        if not s:
            return 0
        while i<len(s):
            count = 1
            while i< len(s) and s[i-1]+1 == s[i] and i >0:
                i +=1
                count +=1
            max_count = max(count,max_count)
            i += 1
        return max_count 
