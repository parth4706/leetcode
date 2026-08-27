class Solution(object):
    def lexGreaterPermutation(self, s, target):
        n = len(s)
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - 97] += 1

        res = []
        for i in range(n):
            x = ord(target[i]) - 97

            if cnt[x]:
                cnt[x] -= 1
                res.append(target[i])
            else:
                break
        else:
            i = n - 1

        while i >= 0:
            if i < len(res):
                cnt[ord(res[i]) - 97] += 1
                res.pop()

            x = ord(target[i]) - 97

            for c in range(x + 1, 26):
                if cnt[c]:
                    res.append(chr(c + 97))
                    cnt[c] -= 1

                    for j in range(26):
                        res.extend([chr(j + 97)] * cnt[j])

                    return ''.join(res)

            i -= 1

        return ""
