class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        Count = 0
        for i in words:
            if i.find(pref) == 0:
                Count += 1
        return Count
