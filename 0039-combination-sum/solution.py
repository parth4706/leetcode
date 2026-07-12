class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        k = []
        res = []
        seen = {}
        def f(idx,x):
            if x == target:
                res.append(k[:])
                return
            if x > target:
                return
            for i in range(idx,len(candidates)):
                k.append(candidates[i])
                f(i,x+candidates[i])
                k.pop()
        f(0,0)
        return res
