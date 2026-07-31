class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c = 0
        i = 0
        while i < len(s):
            if s[i] == "1":
                c += 1
                while i < len(s) and s[i] == "1":
                    i += 1
            if c > 1:
                return False
            i += 1
        return True

