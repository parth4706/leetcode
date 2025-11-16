from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        C = Counter(magazine)
        for i in ransomNote:
            if C[i] > 0:
                C[i] -= 1
            else:
                return False
        return True
