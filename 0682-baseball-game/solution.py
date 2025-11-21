class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x = 0
        res = []
        for i in operations:
            if i.isdigit():
                res.append(int(i))
            elif i == "D":
                res.append(res[-1]*2)
            elif i == "C":
                res.pop(-1)
            elif i == "+":
                res.append(res[-1]+res[-2])
            else:
                res.append(int(i))
            
        return sum(res)
