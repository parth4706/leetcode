class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s11 = s1[::2]
        s12 = s1[1::2]
        s21 = s2[::2]
        s22 = s2[1::2]
        if set(s11) == set(s21):
            if set(s22) == set(s12):
                return True
        return False
