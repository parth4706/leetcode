class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        res = ""
        for i in words:
            res += i
            if res == s:
                return True
        return False

