class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(reverse = True)
        s.sort(reverse = True)
        i = 0
        j = 0
        m = len(g)
        n = len(s)
        c = 0
        while i<m and j < n:
            if g[i] > s[j]:
                i += 1
            else:
                c += 1
                i +=1
                j +=1
        return c
