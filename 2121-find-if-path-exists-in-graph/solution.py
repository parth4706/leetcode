class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        if source == destination:
            return True
        seen =set()
        k = [False]
        def dfs(i):
            if k[0]:
                return
            if i in seen:
                return False
            seen.add(i)
            if i == destination:
                k[0] = True
                return 
            for j in graph[i]:
                dfs(j)
        dfs(source)
        return k[0]
