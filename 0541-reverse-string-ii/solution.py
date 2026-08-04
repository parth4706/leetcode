class Solution(object):
    def reverseStr(self, s, k):
        l = len(s)

        if k >= l:
            return s[::-1]

        res = ""
        i = 0

        while l >= 2*k:
            res += s[i*2*k:i*2*k + k][::-1]
            res += s[i*2*k+k:i*2*k + 2*k]

            l -= 2*k
            i += 1

        if l >= k:
            res += s[i*2*k:i*2*k + k][::-1]
            res += s[i*2*k+k:]
        else:
            res += s[i*2*k:][::-1]

        return res
