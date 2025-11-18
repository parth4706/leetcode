class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])        
        right = float('-inf')
        res = 0
        for pair in pairs:
            if pair[0] > right:
                res += 1
                right = pair[1]
        
        return res
