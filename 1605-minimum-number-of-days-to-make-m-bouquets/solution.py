class Solution(object):
    def minDays(self, bloomDay, m, k):
        def check(day):
            bouquets = 0
            flowers = 0

            for i in range(len(bloomDay)):
                if bloomDay[i] <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            return bouquets >= m

        if m * k > len(bloomDay):
            return -1

        l = min(bloomDay)
        r = max(bloomDay)

        while l <= r:
            mid = l + (r - l) // 2

            if check(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l
