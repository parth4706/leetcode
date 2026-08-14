class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        l = 0
        hm = {}
        i = 0
        while i < len(s):
            hm[s[i]] = hm.get(s[i],0) + 1
            while hm[s[i]] > 2:
                hm[s[l]] -=1
                l += 1
                
            res = max(i-l+1,res)
            i +=1
        return res
