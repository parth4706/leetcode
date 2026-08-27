class Solution(object):
    def isNumber(self, s):
        digit = False
        dot = False
        e = False

        for i, c in enumerate(s):
            if c.isdigit():
                digit = True

            elif c == ".":
                if dot or e:
                    return False
                dot = True

            elif c in "eE":
                if e or not digit:
                    return False
                e = True
                digit = False

            elif c in "+-":
                if i != 0 and s[i - 1] not in "eE":
                    return False

            else:
                return False

        return digit
