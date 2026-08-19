class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        k = 0
        a = []
        p = []
        for i in arr:
            if len(i) == len(set(i)):
                p.append(i)
        for i in p :
            c = 0
            for j in i:
                c += 10**(ord(j)-ord('a'))
            c = str(c)
            a.append(int("0b"+c,2))
        
        s = set()
        res = [0]

        def f(index,x):
            res[0] = max(res[0], bin(x).count("1"))

            for i in range(index,len(a)):
                if x & a[i] == 0:
                    f(i+1,x | a[i])

        f(0,0)
        return res[0]
