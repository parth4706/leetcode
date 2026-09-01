from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        n = len(classroom)
        m = len(classroom[0])

        start = None
        litter_pos = {}
        litter_count = 0

        for i in range(n):
            for j in range(m):
                if classroom[i][j] == "S":
                    start = (i, j)
                elif classroom[i][j] == "L":
                    litter_pos[(i, j)] = litter_count
                    litter_count += 1

        target = (1 << litter_count) - 1

        q = deque()
        q.append((start[0], start[1], energy, 0, 0))

        best = {}
        best[(start[0], start[1], 0)] = energy

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while q:
            i, j, curr, mask, moves = q.popleft()

            if (i, j) in litter_pos:
                mask |= 1 << litter_pos[(i, j)]

            if mask == target:
                return moves

            if curr == 0:
                continue

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if ni < 0 or nj < 0 or ni >= n or nj >= m:
                    continue

                if classroom[ni][nj] == "X":
                    continue

                new_energy = curr - 1

                if classroom[ni][nj] == "R":
                    new_energy = energy

                new_mask = mask

                if (ni, nj) in litter_pos:
                    new_mask |= 1 << litter_pos[(ni, nj)]

                state = (ni, nj, new_mask)

                if state in best and best[state] >= new_energy:
                    continue

                best[state] = new_energy
                q.append((ni, nj, new_energy, new_mask, moves + 1))

        return -1
