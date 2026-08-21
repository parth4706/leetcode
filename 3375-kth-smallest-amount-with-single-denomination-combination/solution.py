class Solution(object):
    def findKthSmallest(self, coins, k):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(coins)
        subsets = []

        for mask in range(1, 1 << n):
            lcm = 1
            bits = 0

            for i in range(n):
                if mask & (1 << i):
                    bits += 1
                    lcm = lcm * coins[i] // gcd(lcm, coins[i])

                    if lcm > 10**18:
                        break

            if lcm <= 10**18:
                subsets.append((lcm, 1 if bits & 1 else -1))

        def count(x):
            total = 0

            for lcm, sign in subsets:
                if lcm <= x:
                    total += sign * (x // lcm)

            return total

        lo = min(coins)
        hi = lo * k

        while lo < hi:
            mid = (lo + hi) // 2

            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo
