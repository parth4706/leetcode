class Solution:
    def sumGame(self, num: str) -> bool:
        left = 0
        right = 0
        cl = 0
        cr = 0

        for i in range(len(num) // 2):
            if num[i] == '?':
                cl += 1
            else:
                left += int(num[i])

        for i in range(len(num) // 2, len(num)):
            if num[i] == '?':
                cr += 1
            else:
                right += int(num[i])
        if cl == cr:
            return left != right
        if(abs(cl-cr)%2==1):
            return True

        return (left - right) != 9 * (cr-cl)//2
