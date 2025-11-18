class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        number_str = str(abs(x)) 
        total_sum = sum(int(digit) for digit in number_str)
        if x%total_sum ==0:
            return total_sum
        else:
            return -1

