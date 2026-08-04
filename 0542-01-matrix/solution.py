from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        res = [[-1] * cols for _ in range(rows)]
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j))
                    res[i][j] = 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while q:
            i, j = q.popleft()

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if (
                    0 <= ni < rows and
                    0 <= nj < cols and
                    res[ni][nj] == -1
                ):
                    res[ni][nj] = res[i][j] + 1
                    q.append((ni, nj))

        return res
