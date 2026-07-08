class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        r = {

        }
        s = s.split()
        if len(s)!= len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in r:
                if r[pattern[i]] != s[i]:
                    return False
            else:
                r[pattern[i]] = s[i]
            
        return True and len(set(pattern)) == len(set(s))
            
