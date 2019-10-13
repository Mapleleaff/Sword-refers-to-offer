"""
题29-顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下 4X4 矩阵：
[[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]]
则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10
"""

class Solution(object):

    # 魔方逆时针旋转思想。
    def RotatePrint(self, matrix):
        result = []
        while matrix:
            result += matrix.pop(0)
            if not matrix:
                break
            matrix = self.turn(matrix)
        return result

    def turn(self, matrix):
        newmat = list(map(list,zip(*matrix)))[::-1]
        return newmat


    # 常规方法，暴力循环。
    def printMatrix(self, matrix):
        if matrix == None:
            return
        rows, columns = len(matrix), len(matrix[0])
        start = 0
        while start * 2 < rows and start * 2 < columns:
            self.PrintMatrixInCircle(matrix, columns, rows, start)
            start += 1
        print('')

    def PrintMatrixInCircle(self, matrix, columns, rows, start):
        row = rows - start
        col = columns - start

        # 从左到右打印一行
        for i in range(start, col):
            number = matrix[start][i]
            print(number, ' ', end='')

        # 从上到下打印一行
        if start < row-1:
            for j in range(start + 1, row):
                number = matrix[j][col-1]
                print(number, ' ', end='')

        # 从右到左打印一行
        if start < col-1 and start < row-1:
            for i in range(col - 2, start - 1, -1):
                number = matrix[row-1][i]
                print(number, ' ', end='')

        # 从下到上打印一行
        if start < col-1 and start < row - 2:
            for j in range(row - 2, start, -1):
                number = matrix[j][start]
                print(number, ' ', end='')


matrix = [[1,  2,  3,  4],
          [5,  6,  7,  8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
matrix2 = [[1],[2],[3],[4],[5]]
matrix3 = [[1,2],
           [3,4],
           [5,6],
           [7,8],
           [9,10]]
S = Solution()
ans = S.RotatePrint(matrix)
print(ans)
S.printMatrix(matrix2)
S.printMatrix(matrix3)
