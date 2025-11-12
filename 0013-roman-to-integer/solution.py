class Solution:
    def romanToInt(self, s: str) -> int:
        k = {
            "M" : 1000,
            "D" : 500,
            "C" : 100,
            "L" : 50,
            "X" : 10,
            "V" : 5,
            "I" : 1 
        }  
        Sum = 0
        i = 0
        n = len(s)
        while i <n:
            if i < n-1 and k[s[i]]< k[s[i+1]]:
                  Sum += k[s[i+1]] - k[s[i]]
                  i += 2
            else:
                Sum += k[s[i]]
                i += 1
        return Sum
