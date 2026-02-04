class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return True if s.count("A")<2 and "LLL" not in s else False
