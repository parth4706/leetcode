class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        seen = {}
        def f(i):
            if i in seen:
                return seen[i]
            if i >= len(questions):
                return 0
            seen[i] = max(questions[i][0] + f(i+1+questions[i][1]),f(i+1))
            return seen[i]
        return f(0)
