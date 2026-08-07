class Solution(object):
    def smallestNumber(self, num, t):
        need = [0, 0, 0, 0]
        primes = [2, 3, 5, 7]

        for i in range(4):
            while t % primes[i] == 0:
                need[i] += 1
                t //= primes[i]

        if t != 1:
            return "-1"

        factors = {
            1: [0,0,0,0],
            2: [1,0,0,0],
            3: [0,1,0,0],
            4: [2,0,0,0],
            5: [0,0,1,0],
            6: [1,1,0,0],
            7: [0,0,0,1],
            8: [3,0,0,0],
            9: [0,2,0,0]
        }

        def remove(req, d):
            f = factors[d]

            return [
                max(0, req[0] - f[0]),
                max(0, req[1] - f[1]),
                max(0, req[2] - f[2]),
                max(0, req[3] - f[3])
            ]

        def possible(req, spaces):
            a, b, c, d = req

            if c + d > spaces:
                return False

            spaces -= c + d

            for six in range(min(a, b) + 1):
                aa = max(0, a - six)
                bb = max(0, b - six)

                twos = (aa + 2) // 3
                threes = (bb + 1) // 2

                if six + twos + threes <= spaces:
                    return True

            return False

        def build(req, k):
            ans = []

            for pos in range(k):
                found = False

                for d in range(1, 10):
                    new = remove(req, d)

                    if possible(new, k - pos - 1):
                        ans.append(str(d))
                        req = new
                        found = True
                        break

                if not found:
                    return None

            if req == [0,0,0,0]:
                return ''.join(ans)

            return None

        n = len(num)

        prefix = [need[:]]
        cur = need[:]

        for ch in num:
            d = int(ch)

            if d == 0:
                prefix.append(None)
            elif prefix[-1] is None:
                prefix.append(None)
            else:
                cur = remove(cur, d)
                prefix.append(cur[:])

        if prefix[n] == [0,0,0,0]:
            return num

        for i in range(n - 1, -1, -1):
            if prefix[i] is None:
                continue

            req = prefix[i]

            for d in range(max(1, int(num[i]) + 1), 10):
                new = remove(req, d)
                spaces = n - i - 1

                if possible(new, spaces):
                    suffix = build(new, spaces)
                    return num[:i] + str(d) + suffix

        length = n + 1

        while not possible(need, length):
            length += 1

        return build(need, length)
