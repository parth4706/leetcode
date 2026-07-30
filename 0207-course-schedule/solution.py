class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            graph[a].append(b)
        visited = set()
        path = set()

        def dfs(i):
            if i in path:
                return False

            if i in visited:
                return True

            path.add(i)

            for nei in graph[i]:
                if not dfs(nei):
                    return False

            path.remove(i)
            visited.add(i)

            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

