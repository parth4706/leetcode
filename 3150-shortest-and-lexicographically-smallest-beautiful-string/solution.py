class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        c = 0
        l = 0
        res = float('inf')
        res1 = 0
        res2 = 0

        for i in range(len(s)):

            if s[i] == '1':
                c += 1

            while c == k:

                length = i - l + 1

                if (length < res or
                    (length == res and s[l:i+1] < s[res1:res2+1])):

                    res = length
                    res1 = l
                    res2 = i

                if s[l] == '1':
                    c -= 1

                l += 1
        if s[res1:res2+1].count("1") != k:
            return ""
        return s[res1:res2+1]
