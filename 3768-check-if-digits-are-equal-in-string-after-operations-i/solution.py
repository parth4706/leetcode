class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        s = [int(ch) for ch in s]

        while len(s) > 2:
            new_s = []
            for i in range(len(s) - 1):
                new_s.append((s[i] + s[i+1]) % 10)
            s = new_s
        if s[0] == s[1]:
            return True
        else:
            return False
        
