class Solution:
    def minMaxDifference(self, num: int) -> int:
        k = None
        for ch in str(num):
            if ch != '9':
                k = ch
                break
        if k is not None:
            max = str(num).replace(k, '9')
        else:
            max = str(num)

        k = None
        for ch in str(num):
            if ch != '0':
                k = ch
                break
        if k is not None:
            min = str(num).replace(k, '0')
        else:
            min = str(num)

        return int(max) - int(min)
