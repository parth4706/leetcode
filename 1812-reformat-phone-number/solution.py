class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace("-","")
        number = number.replace(" ","")
        n = len(number)
        s = ""
        if(len(number)<4):
            return number
        elif(len(number)==4):
            return number[:2] + "-" + number[2:]
        if n%3 == 1:
            for i in range(n//3-1):
                s = s + "-" + number[3*i:3*i+3]
            s = s + "-" + number[3*i+3:3*i+2+3] + "-" + number[3*i+2+3:3*i+4+3]
        elif n %3 == 2:
            for i in range(n//3):
                s = s + "-" + number[3*i:3*i+3]
            s = s + "-" + number[3*i+3:]
        else:
            for i in range(n//3):
                s = s + "-" + number[3*i:3*i+3]
        return s[1:]

