class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        for r, s in reservedSeats:
            rows.setdefault(r, set()).add(s)

        res = 2 * (n - len(rows))

        for seats in rows.values():
            left = 2 not in seats and 3 not in seats and 4 not in seats and 5 not in seats
            middle = 4 not in seats and 5 not in seats and 6 not in seats and 7 not in seats
            right = 6 not in seats and 7 not in seats and 8 not in seats and 9 not in seats

            if left and right:
                res += 2
            elif left or middle or right:
                res += 1

        return res
