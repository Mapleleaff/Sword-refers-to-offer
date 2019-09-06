import numpy as np

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if matrix == None or rows < 1 or cols < 1 or path == None:
            return False

        pathLength = 0
        visited = np.zeros((rows,cols))
        for i in range(rows):
            for j in range(cols):
                if self.hasPathCore(matrix,rows,cols,i,j,path,pathLength,visited):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, i, j, path, pathlength, markmatrix):
        if pathlength == len(path):
            return True

        haspath = False
        if i>=0 and i <rows and j>=0 and j<cols and \
                matrix[i*cols + j] == path[pathlength] and markmatrix[i][j]==0:

            markmatrix[i][j] = 1
            pathlength += 1

            haspath =   self.hasPathCore(matrix,rows,cols,i+1,j,path,pathlength,markmatrix) or \
                        self.hasPathCore(matrix,rows,cols,i,j-1,path,pathlength,markmatrix) or \
                        self.hasPathCore(matrix,rows,cols,i-1,j,path,pathlength,markmatrix) or \
                        self.hasPathCore(matrix,rows,cols,i,j+1,path,pathlength,markmatrix)

            if not haspath:
                pathlength -= 1
                markmatrix[i][j] = 0

        return haspath


s = Solution()
ifTrue = s.hasPath("ABCESFCSADEE", 3, 4, "ABCCED")
ifTrue2 = s.hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS", 5, 8, "SGGFIECVAASABCEHJIGQEM")
print(ifTrue)
print(ifTrue2)

