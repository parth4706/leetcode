class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        k = len(s)
        s1 = ["1" if _ % 2 == 0 else "0" for _ in range(k)]
        s2 = ["1" if _ % 2 == 1 else "0" for _ in range(k)]
        c1 = 0
        c2 = 0
        for i in range(k):
            if s1[i] != s[i]:
                c1 +=1 
            if s2[i] != s[i]:
                c2 += 1
        return min(c1,c2)
