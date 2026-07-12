class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        s = []
        seen = set()
        def f(i):
            if i == len(nums):
                if tuple(sorted(s[:])) in seen:
                    return
                seen.add(tuple(sorted((s[:]))))
                res.append(s[:])
                return
            
            s.append(nums[i])
            f(i+1)
            s.pop()
            f(i+1)

        f(0)
        return res

