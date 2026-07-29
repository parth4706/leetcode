class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def back(s,o,c):
            if (c>n)or (o>n)or (c>o):
                return
            if len(s) == n*2:
                res.append(s)
                return
            back(s + "(",o+1,c)
            back(s + ")",o,c+1)
        back("",0,0)
        return res
