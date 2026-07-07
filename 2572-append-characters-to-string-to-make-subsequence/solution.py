class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        j = 0
        k = len(t) -1
        for i in s:
            if j > k:
                return 0
            if i == t[j]:
                j += 1
        return k - j + 1

        
