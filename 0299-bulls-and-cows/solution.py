from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows= 0
        C1 = Counter(secret)
        C2 = Counter(guess)
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bulls +=1
        for i in C1:
            cows += min(C1[i],C2[i])
        cows -= bulls
        return f"{bulls}A{cows}B"
