class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            for j in range(9):
                num = board[i][j]
                if num in row :
                     return False
                elif num!= '.':
                    row.add(num)


        for i in range(9):
            col = set()
            for j in range(9):
                num = board[j][i]
                if num in col:
                    return False
                elif num != ".":
                    col.add(num)
        

        for i in range(3):
            for j in range(3):
                box = set()
                for k in range(3):
                    for l in range(3):
                        num = board[3*i+k][3*j+l]
                        if num in box:
                            return False
                        elif num!= '.':
                            box.add(num)

        return True
