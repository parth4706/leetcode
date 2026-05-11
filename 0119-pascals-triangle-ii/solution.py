class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        
        for i in range(rowIndex+1):
            row = []
            c = 1
            for k in range(i + 1):
                row.append(c)
                c = c * (i - k) // (k + 1)
            res.append(row)    
        return res[-1]
