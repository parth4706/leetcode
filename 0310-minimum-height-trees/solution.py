from collections import deque

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n <= 2:
            return list(range(n))

        graph = [[] for _ in range(n)]
        degree = [0] * n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

            degree[a] += 1
            degree[b] += 1

        q = deque()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)

        remaining = n

        while remaining > 2:

            size = len(q)
            remaining -= size

            for _ in range(size):
                leaf = q.popleft()

                for nei in graph[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)

        return list(q)
