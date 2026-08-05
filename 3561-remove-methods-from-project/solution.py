class Solution(object):
    def remainingMethods(self, n, k, invocations):
        sus = set()
        seen = set()

        graph = [[] for _ in range(n)]

        for a, b in invocations:
            graph[a].append(b)

        def f(i):
            if i in seen:
                return
            seen.add(i)
            sus.add(i)

            for j in graph[i]:
                f(j)

        f(k)
        for a, b in invocations:
            if a not in sus and b in sus:
                return list(range(n))

        return [i for i in range(n) if i not in sus]
