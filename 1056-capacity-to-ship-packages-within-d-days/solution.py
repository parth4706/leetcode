class Solution(object):
    def shipWithinDays(self, weights, days):
        def check(m):
            capacity = m
            count = 1

            for weight in weights:
                if weight > capacity:
                    count += 1
                    capacity = m

                capacity -= weight

            return count <= days

        l = max(weights)
        r = sum(weights)

        while l <= r:
            m = l + (r - l) // 2

            if check(m):
                r = m - 1
            else:
                l = m + 1

        return l
