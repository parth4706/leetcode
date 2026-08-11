class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        height = [0] * len(matrix[0])
        res = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    height[j] += 1
                else:
                    height[j] = 0

            arr = sorted(height, reverse=True)

            for j in range(len(arr)):
                res = max(res, arr[j] * (j + 1))

        return res
