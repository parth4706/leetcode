class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        c= 0 
        n = len(temperatures)
        temp = [0]*n
        stk = [[temperatures[0],0]]
        for i in range(n):
            while stk and stk[-1][0] < temperatures[i]:
                temp[stk[-1][1]] = i - stk[-1][1]
                stk.pop()
            stk.append([temperatures[i],i])
        return temp
                
