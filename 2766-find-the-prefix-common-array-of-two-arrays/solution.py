class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        s1 = set()
        s2 = set()
        curr = 0
        res = []
        for i in range(len(A)):
            s1.add(B[i])
            s2.add(A[i])
            if A[i] in s1:
                curr +=1
            if B[i] in s2:
                curr +=1
            if A[i] == B[i]:
                curr -= 1
            res.append(curr)
        return res
