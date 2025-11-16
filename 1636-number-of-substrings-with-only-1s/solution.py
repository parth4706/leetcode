class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0
        consecutive = 0
        
        for ch in s:
            if ch == "1":
                consecutive += 1
                count = (count + consecutive) % MOD
            else:
                consecutive = 0
        
        return count
