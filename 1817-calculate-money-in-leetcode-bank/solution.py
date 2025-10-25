class Solution:
    def totalMoney(self, n: int) -> int:
        leet_bank = 0
        day = 0
        deposit = 1
        prev_deposit = 1
        for i in range(n):
            if day == 7:
                day = 0
                prev_deposit += 1
                deposit = prev_deposit

            leet_bank += deposit
            deposit += 1
            day += 1
        return leet_bank


