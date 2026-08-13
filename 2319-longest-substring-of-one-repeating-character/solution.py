class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)

        length = [0] * (4 * n)
        left = [0] * (4 * n)
        right = [0] * (4 * n)
        best = [0] * (4 * n)
        first = [''] * (4 * n)
        last = [''] * (4 * n)

        def merge(node):
            L = node * 2
            R = node * 2 + 1

            length[node] = length[L] + length[R]

            first[node] = first[L]
            last[node] = last[R]

            left[node] = left[L]
            if left[L] == length[L] and last[L] == first[R]:
                left[node] += left[R]

            right[node] = right[R]
            if right[R] == length[R] and last[L] == first[R]:
                right[node] += right[L]

            best[node] = max(best[L], best[R])

            if last[L] == first[R]:
                best[node] = max(
                    best[node],
                    right[L] + left[R]
                )

        def build(node, l, r):
            if l == r:
                length[node] = 1
                left[node] = 1
                right[node] = 1
                best[node] = 1
                first[node] = s[l]
                last[node] = s[l]
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            merge(node)

        def update(node, l, r, index, char):
            if l == r:
                first[node] = char
                last[node] = char
                left[node] = 1
                right[node] = 1
                best[node] = 1
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, r, index, char)

            merge(node)

        build(1, 0, n - 1)

        ans = []

        for i in range(len(queryCharacters)):
            update(1, 0, n - 1, queryIndices[i], queryCharacters[i])
            ans.append(best[1])

        return ans
