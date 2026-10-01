class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if i == "(" or i == "[" or i=="{":
                l.append(i)
            try:
                if i == ")":
                    k = l.pop()
                    if k != "(":
                        return False
                elif i == "}":
                    k = l.pop()
                    if k != "{":
                        return False
                elif i == "]":
                    k = l.pop()
                    if k != "[":
                        return False 
            except IndexError:
                return False
        if l:
            return False
        return True

