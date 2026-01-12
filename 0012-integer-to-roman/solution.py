class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        integers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        res = ""
        for i in range(13):
            while(num>=integers[i]):
                num -= integers[i]
                res += roman[i]
        
        return res
        
