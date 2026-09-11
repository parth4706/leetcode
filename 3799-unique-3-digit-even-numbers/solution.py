class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        s = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if k!=i and j != i and j != k:
                        s.add(str(digits[i])+str(digits[j])+str(digits[k]))
        res = 0
        for i in s:
            if int(i)%2==0 and len(str(int(i)))==3:
                res += 1
        return res
