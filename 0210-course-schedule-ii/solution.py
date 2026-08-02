class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        visits = [0]*(numCourses)
        res = []
        def f(node):
            if visits[node] == 2: 
                return True
            elif visits[node] == 1:
                return False
            visits[node] = 1
            for i in graph[node]:
                if not f(i):
                    return False
            visits[node] = 2
            res.append(node)
            return True
        for i in range(numCourses):
            if not f(i):
                return []
        return res

