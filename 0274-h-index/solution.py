class Solution:
    def hIndex(self, citations: List[int]) -> int:
        P = 0 
        i = 0
        H = 0
        while i <= len(citations):
            count = 0
            for x in citations:
                if x >= H:
                    count += 1
            if count >= H:
                H+=1
            else:
                break
            i += 1
        return H-1
