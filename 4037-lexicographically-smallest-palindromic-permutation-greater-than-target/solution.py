class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        n = len(s)
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - 97] += 1

        odd = -1
        for i in range(26):
            if cnt[i] % 2:
                if odd != -1:
                    return ""
                odd = i

        half = [x // 2 for x in cnt]
        h = n // 2

        def palindrome(left):
            return left + (chr(odd + 97) if odd != -1 else "") + left[::-1]

        left = []
        i = 0

        while i < h:
            x = ord(target[i]) - 97

            if half[x]:
                left.append(target[i])
                half[x] -= 1
                i += 1
            else:
                break

        if i == h:
            p = palindrome(''.join(left))
            if p > target:
                return p
            i -= 1

        while i >= 0:
            if i < len(left):
                half[ord(left[i]) - 97] += 1
                left.pop()

            x = ord(target[i]) - 97

            for c in range(x + 1, 26):
                if half[c]:
                    left.append(chr(c + 97))
                    half[c] -= 1

                    for j in range(26):
                        left.extend([chr(j + 97)] * half[j])

                    return palindrome(''.join(left))

            i -= 1

        return ""
