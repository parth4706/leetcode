class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        for i in range(numRows):
            row = []
            c = 1
            for k in range(i + 1):
                row.append(c)
                c = c * (i - k) // (k + 1)
            res.append(row)    
        return res
